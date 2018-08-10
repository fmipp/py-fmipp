from distutils.core import setup
from distutils.extension import Extension
from distutils.command.build import build
import platform
import os

#rectifying build order for swig .i files-----
class CustomBuild(build):
    sub_commands = [
        ('build_ext', build.has_ext_modules),
        ('build_py', build.has_pure_modules),
        ('build_clib', build.has_c_libraries),
        ('build_scripts', build.has_scripts),
    ]
##--------------------------------------------


#check platform specifications----
if platform.system()=='Linux':
  fmu_bin_ext = '\".so\"'
  if '32bit' in platform.architecture():
    install_platform = 'linux32'
  else:
    install_platform = 'linux64'

if platform.system()=='Windows':
  fmu_bin_ext = '\".dll\"'
  if '32bit' in platform.architecture():
    install_platform = 'win32'
  else:
    install_platform = 'win64'

if platform.system()== 'Darwin':
  fmu_bin_ext = '\".dylib\"'
  if '32bit' in platform.architecture():
    install_platform = 'darwin32'
  else:
    install_platform = 'darwin64'
fmu_bin_dir = '\"' + install_platform + '\"'
##--------------------------------


macros=[('FMU_BIN_DIR',                   fmu_bin_dir),
        ('FMU_BIN_EXT',                   fmu_bin_ext),
        ('fmippim_EXPORTS',               None),
        ('FRONT_END_TYPE',                'FMIComponentFrontEnd'),
        ('FRONT_END_TYPE_INCLUDE',        '\"export/include/FMIComponentFrontEnd.h\"'),
        ('fmi2EXPORTS',                   None),
        ('fmippim_wrap_java_Exports',     None),
        ('EPS_TIME',                      '1e-9'),
        ('FMU_URI_PRE',                   '\"\"'),    #not directly used?
        ('givezero_EXPORTS',              None),
        ('zigzag_EXPORTS',                None),
        ('zigzag2_EXPORTS',               None),
        ('zigzag2_me_only_EXPORTS',       None),
        ('FMI2_NO_COSIMULATION_FUNCTION', None),
        ('step_t0_EXPORTS',               None),
        ('MODEL_IDENTIFIER',              'sine_standalone2'),
        ('sine_standalone2_EXPORTS',      None),
        ('sine_standalone_EXPORTS',       None),
        ('v2_0_EXPORTS',                  None),
        ('bouncingBall_EXPORTS',          None),
        ('dq_EXPORTS',                    None),
        ('vanDerPol_EXPORTS',             None),
        ('values_EXPORTS',                None),
        ('stiff_EXPORTS',                 None),
        ('linear_stiff_EXPORTS',          None),
        ('stiff2_EXPORTS',                None),
        ('polynomial_EXPORTS',            None),
        ('asymptotic_sine_EXPORTS',       None),
        ('robertson_EXPORTS',             None),
        ('dxiskx_EXPORTS',                None),
        ('zerocrossing_EXPORTS',          None),
        ('USE_SUNDIALS',                  None),
        ('SWIGPYTHON',                    None),
        ('PATH_SEPARATOR',                ':'),
        ('CMAKE_CXX_FLAGS',               '-std=c++11'),
        ('FMIPP_WRAP_PYTHON_MODULE',      'fmipp_wrap_python'),
        ('SWIG_PYTHON_2_UNICODE',         None),
       ]

#PATHS------------------------------------------------------------------------------------------------
export_functions = ['source/fmipp/export/functions/fmi_v1.0/fmiFunctions.cpp', 'source/fmipp/export/functions/fmi_v2.0/fmi2Functions.cpp']
export_src = ['source/fmipp/export/src/BackEndApplicationBase.cpp', 'source/fmipp/export/src/FMIComponentBackEnd.cpp', 'source/fmipp/export/src/FMIComponentFrontEnd.cpp', 'source/fmipp/export/src/FMIComponentFrontEndBase.cpp', 'source/fmipp/export/src/HelperFunctions.cpp', 'source/fmipp/export/src/IPCLogger.cpp', 'source/fmipp/export/src/IPCMasterLogger.cpp', 'source/fmipp/export/src/IPCSlaveLogger.cpp', 'source/fmipp/export/src/ScalarVariable.cpp', 'source/fmipp/export/src/SHMManager.cpp', 'source/fmipp/export/src/SHMMaster.cpp', 'source/fmipp/export/src/SHMSlave.cpp']
import_base_src = ['source/fmipp/import/base/src/BareFMU.cpp', 'source/fmipp/import/base/src/CallbackFunctions.cpp', 'source/fmipp/import/base/src/DynamicalSystem.cpp', 'source/fmipp/import/base/src/FMUCoSimulation_v1.cpp', 'source/fmipp/import/base/src/FMUCoSimulation_v2.cpp', 'source/fmipp/import/base/src/FMUModelExchange_v1.cpp', 'source/fmipp/import/base/src/FMUModelExchange_v2.cpp', 'source/fmipp/import/base/src/LogBuffer.cpp', 'source/fmipp/import/base/src/ModelDescription.cpp', 'source/fmipp/import/base/src/ModelManager.cpp', 'source/fmipp/import/base/src/PathFromUrl.cpp']
import_integrators_src = ['source/fmipp/import/integrators/src/Integrator.cpp', 'source/fmipp/import/integrators/src/IntegratorStepper.cpp']
import_utility_src = ['source/fmipp/import/utility/src/FixedStepSizeFMU.cpp', 'source/fmipp/import/utility/src/History.cpp', 'source/fmipp/import/utility/src/IncrementalFMU.cpp', 'source/fmipp/import/utility/src/InterpolatingFixedStepSizeFMU.cpp', 'source/fmipp/import/utility/src/RollbackFMU.cpp', 'source/fmipp/import/utility/src/VariableStepSizeFMU.cpp']
all_cpp = export_functions + export_src + import_base_src + import_integrators_src + import_utility_src

libfmippex_i = ['source/fmipp/export/swig/libfmippex.i']
libfmippim_i = ['source/fmipp/import/swig/libfmippim.i']

##----------------------------------------------------------------------------------------------------

#Other --------------------
libfmipp_fmu_frontendlib_sources = ['source/fmipp/export/src/FMIComponentFrontEnd.cpp', 'source/fmipp/export/src/FMIComponentFrontEndBase.cpp', 'source/fmipp/export/src/IPCLogger.cpp', 'source/fmipp/export/src/IPCMasterLogger.cpp', 'source/fmipp/export/src/HelperFunctions.cpp','source/fmipp/export/src/ScalarVariable.cpp', 'source/fmipp/import/base/src/ModelDescription.cpp', 'source/fmipp/import/base/src/PathFromUrl.cpp']

fmi2dll_sources = ['source/fmipp/export/functions/fmi_v2.0/fmi2Functions.cpp', 'source/fmipp/export/src/ScalarVariable.cpp', 'source/fmipp/export/src/FMIComponentFrontEnd.cpp', 'source/fmipp/export/src/FMIComponentFrontEndBase.cpp', 'source/fmipp/export/src/IPCLogger.cpp', 'source/fmipp/export/src/IPCMasterLogger.cpp', 'source/fmipp/export/src/SHMMaster.cpp', 'source/fmipp/export/src/SHMManager.cpp', 'source/fmipp/export/src/HelperFunctions.cpp', 'source/fmipp/import/base/src/ModelDescription.cpp', 'source/fmipp/import/base/src/PathFromUrl.cpp']

include_directorys = ['source/fmipp/', 'source/fmipp/common/', 'source/fmipp/common/fmi_v1.0/', 'source/fmipp/common/fmi_v2.0/', 'source/fmipp/export/include/', 'source/fmipp/import/base/include/', 'source/fmipp/import/integrators/include/', 'source/fmipp/import/utility/include/']

additional_libs = ['boost_filesystem', 'boost_system','sundials_cvode', 'sundials_nvecserial'] 
library_dir = [os.path.join(os.path.dirname(__file__),'fmipp','lib')]





#Modules------------------------------------------------------------------------------------
importpyd =                Extension('fmipp/lib/_fmippim',
                                     swig_opts = ['-c++', '-Isource/fmipp/', '-outdir','fmipp', '-DUSE_SUNDIALS'],
                                     sources = libfmippim_i + import_base_src + import_integrators_src + import_utility_src,
                                     include_dirs = include_directorys,
                                     define_macros = macros,
                                     undef_macros = ['NDEBUG'],
                                     library_dirs = library_dir,
                                     libraries = additional_libs,
                                     extra_compile_args = ['-g0'],
                                    )
exportpyd =                Extension('fmipp/export/_fmippex',
                                     swig_opts = ['-c++', '-Isource/fmipp/', '-outdir','fmipp/export', '-DUSE_SUNDIALS'],
                                     sources = libfmippex_i + all_cpp,
                                     include_dirs = include_directorys,
                                     define_macros = macros,
                                     undef_macros = ['NDEBUG'],
                                     library_dirs = library_dir,
                                     libraries = additional_libs,
                                     extra_compile_args = ['-g0'],
                                    )
importdll =                Extension('fmipp/lib/libfmippim',
                                     sources = import_base_src + import_integrators_src + import_utility_src,
                                     include_dirs = include_directorys,
                                     define_macros = macros,
                                     undef_macros = ['NDEBUG'],
                                     extra_compile_args = ['-g0'],
                                    )
exportdll =                Extension('fmipp/lib/libfmippex',
                                     sources = export_src,
                                     include_dirs = include_directorys,
                                     define_macros = macros,
                                     undef_macros = ['NDEBUG'],
                                     extra_compile_args = ['-g0'],
                                    )

fmi2dll =                  Extension('fmipp/export/bin/libfmi2',
                                     sources = fmi2dll_sources,
                                     include_dirs = include_directorys,
                                     define_macros = macros,
                                     undef_macros = ['NDEBUG'],
                                     library_dirs = library_dir,
                                     libraries = additional_libs,
                                     extra_compile_args = ['-g0'],
                                    )
libfmipp_fmu_frontendlib = Extension('fmipp/export/bin/libfmipp_fmu_frontend',
                                     sources = libfmipp_fmu_frontendlib_sources,
                                     include_dirs = include_directorys + os.getenv('Path',default='').split(os.pathsep),
                                     define_macros = macros,
                                     undef_macros = ['NDEBUG'],
                                     extra_compile_args = ['-g0'],
                                    )
##------------------------------------------------------------------------------------------


setup(name = 'fmipp',
      version = '1.3',
      description = 'FMI++ Python Interface for Windows',
      long_description = 'This package provides a Python wrapper for the FMI++ library, which \nintends to bridge the gap between the basic fuctionality provided by \nthe FMI                specification and the typical requirements of simulation tools.',
#      long_description = pyfmipp_long_description,
      url = 'http://fmipp.sourceforge.net',
      maintainer = 'Edmund Widl',
      maintainer_email = 'edmund.widl@ait.ac.at',
      license = 'BSD license & BOOST software license',
      platforms = 'Windows',
      keywords = [ 'FMI', 'Functional Mock-up Interface', 'FMI++ Library' ],
      classifiers = [
         'Development Status :: 4 - Beta',
         'Intended Audience :: Science/Research',
         'Operating System :: Microsoft :: Windows',
         'Topic :: Scientific/Engineering',
         'Programming Language :: Python :: 3.5',
         'Programming Language :: C++',
        ],
      cmdclass = {'build': CustomBuild},
      packages = [ 'fmipp', 'fmipp.export', 'fmipp.test'],
      ext_modules = [importpyd, exportpyd, importdll, exportdll, fmi2dll, libfmipp_fmu_frontendlib],
      include_package_data = True,
     )