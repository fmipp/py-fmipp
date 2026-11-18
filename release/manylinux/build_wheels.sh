#!/bin/bash
# Build manylinux wheels for CPython 3.10–3.13 from a checkout mounted at /io.
# SUNDIALS and Boost are the static libraries installed in the image.

set -euo pipefail

IO_ROOT="${IO_ROOT:-/io}"
SUNDIALS_ROOT="${SUNDIALS_ROOT:-/opt/sundials-3.1.2}"
BOOST_ROOT="${BOOST_ROOT:-/opt/boost-1.72}"
export SUNDIALS_ROOT BOOST_ROOT

if [[ ! -f "${IO_ROOT}/py-fmipp/setup.py" || ! -d "${IO_ROOT}/fmipp" ]]; then
  echo "Mount the fmipp-dev repository at /io. It must contain py-fmipp/ and fmipp/." >&2
  exit 1
fi

WORK="$(mktemp -d)"
cleanup() {
  rm -rf "${WORK}"
}
trap cleanup EXIT

echo "Copying sources into ${WORK}"
tar -C "${IO_ROOT}/py-fmipp" \
  --exclude build \
  --exclude dist \
  --exclude .pytest_cache \
  --exclude fmipp.egg-info \
  --exclude source/fmipp \
  -cf - . | tar -C "${WORK}" -xf -
rm -rf "${WORK}/source/fmipp"
mkdir -p "${WORK}/source/fmipp"
tar -C "${IO_ROOT}/fmipp" --exclude .git -cf - . | tar -C "${WORK}/source/fmipp" -xf -
find "${WORK}/fmipp" -type f \( -name '*.dll' -o -name '*.pyd' -o -name '*.lib' -o -name '*.exp' \) -delete

mkdir -p "${IO_ROOT}/py-fmipp/dist"
rm -f "${IO_ROOT}/py-fmipp/dist"/fmipp-*-manylinux*.whl

shopt -s nullglob
pythons=( /opt/python/cp310-cp310* /opt/python/cp311-cp311* /opt/python/cp312-cp312* /opt/python/cp313-cp313* )
if [[ ${#pythons[@]} -eq 0 ]]; then
  echo "No CPython 3.10–3.13 installations under /opt/python." >&2
  exit 1
fi

audit_python=""
for pyroot in "${pythons[@]}"; do
  if [[ -x "${pyroot}/bin/python" ]]; then
    audit_python="${pyroot}/bin/python"
  fi
done
"${audit_python}" -m pip install -U 'auditwheel>=6'

check_wheel() {
  local wheel="$1"
  local extract so
  case "${wheel}" in
    *manylinux2014*|*manylinux_2_17*) ;;
    *)
      echo "Wheel ${wheel} is missing a manylinux platform tag." >&2
      exit 1
      ;;
  esac
  extract="$(mktemp -d)"
  unzip -q "${wheel}" -d "${extract}"
  local found=0
  while IFS= read -r so; do
    found=1
    echo "ldd ${so#${extract}/}"
    ldd "${so}"
    if ldd "${so}" | grep -E 'libsundials|libboost|not found'; then
      echo "ERROR: ${so} still depends on SUNDIALS or Boost, or a library is missing." >&2
      rm -rf "${extract}"
      exit 1
    fi
  done < <(find "${extract}" -name '*.so' -o -name '*.so.*')
  rm -rf "${extract}"
  if [[ "${found}" -eq 0 ]]; then
    echo "No extension modules found in ${wheel}." >&2
    exit 1
  fi
}

run_tests() {
  local py="$1"
  local wheel="$2"
  local test_dir
  "${py}" -m pip install --force-reinstall "${wheel}"
  test_dir="$(mktemp -d)"
  cp -a "${IO_ROOT}/py-fmipp/test/." "${test_dir}/"
  rm -rf "${test_dir}/zigzag" "${test_dir}/zigzag2" "${test_dir}/FMUExportTestCS" "${test_dir}/__pycache__"
  (
    cd "${test_dir}"
    PYTHONPATH="" "${py}" -m pytest --rootdir="${test_dir}" -p no:cacheprovider test_pyfmipp.py
  )
  rm -rf "${test_dir}"
}

built=0
for pyroot in "${pythons[@]}"; do
  if [[ ! -x "${pyroot}/bin/python" ]]; then
    echo "Skipping ${pyroot} (not in this image)."
    continue
  fi
  py="${pyroot}/bin/python"
  echo "===== Building $(basename "${pyroot}") ====="
  "${py}" -m pip install -U pip setuptools wheel pytest
  rm -rf "${WORK}/build" "${WORK}/dist" "${WORK}/fmipp.egg-info"
  ( cd "${WORK}" && "${py}" setup.py bdist_wheel )

  wheels=( "${WORK}/dist"/fmipp-*.whl )
  if [[ ${#wheels[@]} -ne 1 ]]; then
    echo "Expected one wheel in ${WORK}/dist, found ${#wheels[@]}." >&2
    exit 1
  fi

  log="$(mktemp)"
  set +e
  "${audit_python}" -m auditwheel repair "${wheels[0]}" -w "${IO_ROOT}/py-fmipp/dist" >"${log}" 2>&1
  status=$?
  set -e
  cat "${log}"
  if [[ "${status}" -ne 0 ]]; then
    echo "auditwheel repair failed." >&2
    exit "${status}"
  fi
  repaired="$(sed -n 's/^Fixed-up wheel written to //p' "${log}" | tail -1)"
  rm -f "${log}"
  if [[ -z "${repaired}" || ! -f "${repaired}" ]]; then
    echo "auditwheel did not report the repaired wheel." >&2
    exit 1
  fi

  check_wheel "${repaired}"
  run_tests "${py}" "${repaired}"
  built=$((built + 1))
done

if [[ "${built}" -eq 0 ]]; then
  echo "No wheels were built." >&2
  exit 1
fi

echo "Built ${built} wheel(s) in ${IO_ROOT}/py-fmipp/dist:"
ls -lh "${IO_ROOT}/py-fmipp/dist"/fmipp-*-manylinux*.whl
