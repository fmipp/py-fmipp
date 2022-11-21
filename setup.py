# -----------------------------------------------------------------
# Copyright (c) 2022, AIT Austrian Institute of Technology GmbH.
# All rights reserved. See file FMIPP_LICENSE.txt for details.
# -----------------------------------------------------------------

'''
Run this script to create binary wheels and source distribution packages for the FMI++ Python Interface.

Create binary wheel on Windows:
> python setup.py bdist_wheel --python-tag py<X.Y> -p <platform_tag>

Create source distribution package on Linux:
> python setup.py sdist

See file README.md for more information.
'''

import platform
import os
import sys

#
# Meta information for FMI++ Python package.
#

_name = 'fmipp'
_version = '2.0.2'
_description = 'FMI++ Python Interface'
_url = 'https://fmipp.readthedocs.io/projects/py-fmipp'
_maintainer = 'Edmund Widl'
_maintainer_email = 'edmund.widl@ait.ac.at'
_license = 'BSD license & BOOST software license'

_keywords = [
  'FMI',
  'Functional Mock-up Interface',
  'FMI++ Library',
]

_classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Science/Research',
  'Operating System :: Microsoft :: Windows',
  'Operating System :: POSIX :: Linux',
  'Topic :: Scientific/Engineering',
  'Programming Language :: Python :: 2.7',
  'Programming Language :: Python :: 3.10',
  'Programming Language :: C++',
]

_packages = [
  'fmipp',
  'fmipp.export'
]

# Read long description from file (reStructuredText syntax). Will be parsed and displayed as HTML online.
with open( 'description.txt' ) as description_file:
  _long_description = description_file.read()



def create_windows_wheel():
  '''
  Setup for binary wheels (Windows).
  '''

  # Load setuptools package.
  from setuptools import setup
  from setuptools.dist import Distribution

  # Base configuration for packaging.
  class BinaryDistribution( Distribution ):
    def is_pure( self ):
      return False

  ## List of additional files (i.e., files without the '.py' extension) that are part of the distribution.
  #pyfmipp_additional_files = [
  #  'lib/...',
  #]

  # Run setup.
  setup(
    name = _name,
    version = _version,
    description = _description,
    long_description = _long_description,
    url = _url,
    maintainer = _maintainer,
    maintainer_email = _maintainer_email,
    license = 'BSD license & BOOST software license',
    platforms = [ 'Windows' ],
    keywords = _keywords,
    classifiers = _classifiers,
    packages = _packages,
    #package_data = { 'fmipp': pyfmipp_additional_files },
    include_package_data = True,
    distclass = BinaryDistribution,
  )



def create_source_distribution( fmu_bin_ext, install_platform ):
  '''
  Setup for source distribution packages (Linux).
  '''

  # Load distutils package.
  from distutils.core import setup
  from distutils.extension import Extension
  from distutils.command.build import build

  # Base configuration for packaging.
  class CustomBuild( build ):
    sub_commands = [
      ( 'build_ext', build.has_ext_modules ),
      ( 'build_py', build.has_pure_modules ),
      ( 'build_clib', build.has_c_libraries ),
      ( 'build_scripts', build.has_scripts ),
    ]

  # Define compiler macros.
  macros = [
    ( 'FMU_BIN_DIR', '\"' + install_platform + '\"' ),
    ( 'FMU_BIN_EXT', fmu_bin_ext ),
    ( 'FRONT_END_TYPE', 'FMIComponentFrontEnd' ),
    ( 'FRONT_END_TYPE_INCLUDE', '\"export/include/FMIComponentFrontEnd.h\"' ),
    ( 'USE_SUNDIALS', None ),
  ]

  import_base_src = [
    'source/fmipp/import/base/src/BareFMU.cpp',
    'source/fmipp/import/base/src/CallbackFunctions.cpp',
    'source/fmipp/import/base/src/DynamicalSystem.cpp',
    'source/fmipp/import/base/src/FMUCoSimulation_v1.cpp',
    'source/fmipp/import/base/src/FMUCoSimulation_v2.cpp',
    'source/fmipp/import/base/src/FMUModelExchange_v1.cpp',
    'source/fmipp/import/base/src/FMUModelExchange_v2.cpp',
    'source/fmipp/import/base/src/LogBuffer.cpp',
    'source/fmipp/import/base/src/ModelDescription.cpp',
    'source/fmipp/import/base/src/ModelManager.cpp',
    'source/fmipp/import/base/src/PathFromUrl.cpp'
  ]

  import_integrators_src = [
    'source/fmipp/import/integrators/src/Integrator.cpp',
    'source/fmipp/import/integrators/src/IntegratorStepper.cpp'
  ]

  import_utility_src = [
    'source/fmipp/import/utility/src/FixedStepSizeFMU.cpp',
    'source/fmipp/import/utility/src/History.cpp',
    'source/fmipp/import/utility/src/IncrementalFMU.cpp',
    'source/fmipp/import/utility/src/InterpolatingFixedStepSizeFMU.cpp',
    'source/fmipp/import/utility/src/RollbackFMU.cpp',
    'source/fmipp/import/utility/src/VariableStepSizeFMU.cpp'
  ]

  export_src = [
    'source/fmipp/export/src/BackEndApplicationBase.cpp',
    'source/fmipp/export/src/FMIComponentBackEnd.cpp',
    'source/fmipp/export/src/FMIComponentFrontEnd.cpp',
    'source/fmipp/export/src/FMIComponentFrontEndBase.cpp',
    'source/fmipp/export/src/HelperFunctions.cpp',
    'source/fmipp/export/src/IPCLogger.cpp',
    'source/fmipp/export/src/IPCMasterLogger.cpp',
    'source/fmipp/export/src/IPCSlaveLogger.cpp',
    'source/fmipp/export/src/ScalarVariable.cpp',
    'source/fmipp/export/src/SHMManager.cpp',
    'source/fmipp/export/src/SHMMaster.cpp',
    'source/fmipp/export/src/SHMSlave.cpp',
    'source/fmipp/import/base/src/ModelDescription.cpp',
    'source/fmipp/import/base/src/PathFromUrl.cpp',
  ]

  libfmippex_swig = [
    'source/fmipp/export/swig/libfmippex.i'
  ]

  libfmippim_swig = [
    'source/fmipp/import/swig/libfmippim.i'
  ]

  fmi1_frontendlib_src = [
    'source/fmipp/export/src/FMIComponentFrontEnd.cpp',
    'source/fmipp/export/src/FMIComponentFrontEndBase.cpp',
    'source/fmipp/export/src/IPCLogger.cpp',
    'source/fmipp/export/src/IPCMasterLogger.cpp',
    'source/fmipp/export/src/HelperFunctions.cpp',
    'source/fmipp/export/src/ScalarVariable.cpp',
    'source/fmipp/import/base/src/ModelDescription.cpp',
    'source/fmipp/import/base/src/PathFromUrl.cpp'
  ]

  fmi2_frontend_src = [
    'source/fmipp/export/functions/fmi_v2.0/fmi2Functions.cpp',
    'source/fmipp/export/src/ScalarVariable.cpp',
    'source/fmipp/export/src/FMIComponentFrontEnd.cpp',
    'source/fmipp/export/src/FMIComponentFrontEndBase.cpp',
    'source/fmipp/export/src/IPCLogger.cpp',
    'source/fmipp/export/src/IPCMasterLogger.cpp',
    'source/fmipp/export/src/SHMMaster.cpp',
    'source/fmipp/export/src/SHMManager.cpp',
    'source/fmipp/export/src/HelperFunctions.cpp',
    'source/fmipp/import/base/src/ModelDescription.cpp',
    'source/fmipp/import/base/src/PathFromUrl.cpp'
  ]

  include_dirs = [
    'source/fmipp/',
    os.path.join( os.path.dirname( __file__ ), 'source', 'fmipp' )
  ]

  extra_link_args = [
    '-lrt',
    '-lboost_filesystem',
    '-lboost_system',
    '-lsundials_cvode',
    '-lsundials_nvecserial'
  ]

  extra_compile_args = [
    '-g0',
    '-std=c++11'
  ]

  # Define FMI++ import wrapper module.
  import_wrapper = Extension(
    'fmipp/lib/_fmippim',
    swig_opts = [ '-c++', '-Isource/fmipp', '-outdir', 'fmipp', '-DUSE_SUNDIALS' ],
    sources = libfmippim_swig + import_base_src + import_integrators_src + import_utility_src,
    include_dirs = include_dirs,
    define_macros = macros,
    undef_macros = [ 'NDEBUG' ],
    extra_compile_args = extra_compile_args,
    extra_link_args = extra_link_args,
  )

  # Define FMI++ export wrapper module.
  export_wrapper = Extension(
    'fmipp/export/_fmippex',
    swig_opts = [ '-c++', '-Isource/fmipp', '-outdir', 'fmipp/export' ],
    sources = libfmippex_swig + export_src,
    include_dirs = include_dirs,
    define_macros = macros,
    undef_macros = [ 'NDEBUG' ],
    extra_compile_args = extra_compile_args,
    extra_link_args = extra_link_args,
  )

  # Define module for FMI 2.0 front-end (FMU export).
  fmi2_frontend = Extension(
    'fmipp/export/bin/libfmi2',
    sources = fmi2_frontend_src,
    include_dirs = include_dirs,
    define_macros = macros,
    undef_macros = [ 'NDEBUG' ],
    extra_compile_args = extra_compile_args,
    extra_link_args = extra_link_args,
  )

  # Define module for FMI 1.0 front-end library (FMU export).
  fmi1_frontend_lib = Extension(
    'fmipp/export/bin/libfmipp_fmu_frontend',
    sources = fmi1_frontendlib_src,
    include_dirs = include_dirs + os.getenv( 'Path', default='' ).split( os.pathsep ),
    define_macros = macros,
    undef_macros = ['NDEBUG'],
    extra_compile_args = extra_compile_args,
    extra_link_args  = [ '-lrt' ],
  )

  # List of additional files.
  pyfmipp_additional_files = [
    'licenses/FMIPP_LICENSE.txt',
    'licenses/BOOST_SOFTWARE_LICENSE.txt',
    'licenses/SUNDIALS_LICENSE.txt',
  ]

  # Run setup.
  setup(
    name = _name,
    version = _version,
    description = _description,
    long_description = _long_description,
    url = _url,
    maintainer = _maintainer,
    maintainer_email = _maintainer_email,
    license = 'BSD license & BOOST software license',
    platforms = [ 'any' ],
    keywords = _keywords,
    classifiers = _classifiers,
    packages = _packages,
    package_data = { 'fmipp': pyfmipp_additional_files },
    include_package_data = True,
    cmdclass = { 'build': CustomBuild },
    ext_modules = [
      import_wrapper,
      export_wrapper,
      fmi2_frontend,
      fmi1_frontend_lib
    ],
  )



if __name__ == '__main__':


  #
  # Platform specifications.
  #

  if platform.system()=='Windows':

    # Create binary wheels for Windows.
    create_windows_wheel()

  elif platform.system()== 'Darwin':

    # Create source distribution packages for OSX.
    if '32bit' in platform.architecture():
      create_source_distribution( fmu_bin_ext = '\".dylib\"', install_platform = 'darwin32' )
    else:
      create_source_distribution( fmu_bin_ext = '\".dylib\"', install_platform = 'darwin64' )

  elif platform.system()== 'Linux':

    # Create source distribution packages for Linux.
    if '32bit' in platform.architecture():
      create_source_distribution( fmu_bin_ext = '\".so\"', install_platform = 'linux32' )
    else:
      create_source_distribution( fmu_bin_ext = '\".so\"', install_platform = 'linux64' )
