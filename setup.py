import platform
import os
import sys


#check platform specifications----
use_win_wheels = False
if platform.system()=='Linux':
  fmu_bin_ext = '\".so\"'
  if '32bit' in platform.architecture():
    install_platform = 'linux32'
  else:
    install_platform = 'linux64'
#endif
if platform.system()=='Windows':
  use_win_wheels = True
  fmu_bin_ext = '\".dll\"'
  if '32bit' in platform.architecture():
    install_platform = 'win32'
  else:
    install_platform = 'win64'
#endif
if platform.system()== 'Darwin':
  fmu_bin_ext = '\".dylib\"'
  if '32bit' in platform.architecture():
    install_platform = 'darwin32'
  else:
    install_platform = 'darwin64'
fmu_bin_dir = '\"' + install_platform + '\"'
#endif
##--------------------------------

#platform dependant options--------------------------------
if use_win_wheels:
  from setuptools import setup
  from setuptools.dist import Distribution

  class BinaryDistribution(Distribution):
    def is_pure(self):
      return False
else: # for linux
  from distutils.core import setup
  from distutils.extension import Extension
  from distutils.command.build import build

  class CustomBuild(build):
      sub_commands = [
                      ('build_ext', build.has_ext_modules),
                      ('build_py', build.has_pure_modules),
                      ('build_clib', build.has_c_libraries),
                      ('build_scripts', build.has_scripts),
                     ]
#endif
##---------------------------------------------------------


macros=[('FMU_BIN_DIR',                   fmu_bin_dir),
        ('FMU_BIN_EXT',                   fmu_bin_ext),
        ('FRONT_END_TYPE',                'FMIComponentFrontEnd'),
        ('FRONT_END_TYPE_INCLUDE',        '\"export/include/FMIComponentFrontEnd.h\"'),
        ('FMU_URI_PRE',                   '\"\"'),
        ('USE_SUNDIALS',                  None),
        ('SWIGPYTHON',                    None),
       ]

#PATHS------------------------------------------------------------------------------------------------
export_functions = ['source/fmipp-code/export/functions/fmi_v1.0/fmiFunctions.cpp', 'source/fmipp-code/export/functions/fmi_v2.0/fmi2Functions.cpp']
export_src = ['source/fmipp-code/export/src/BackEndApplicationBase.cpp', 'source/fmipp-code/export/src/FMIComponentBackEnd.cpp', 'source/fmipp-code/export/src/FMIComponentFrontEnd.cpp', 'source/fmipp-code/export/src/FMIComponentFrontEndBase.cpp', 'source/fmipp-code/export/src/HelperFunctions.cpp', 'source/fmipp-code/export/src/IPCLogger.cpp', 'source/fmipp-code/export/src/IPCMasterLogger.cpp', 'source/fmipp-code/export/src/IPCSlaveLogger.cpp', 'source/fmipp-code/export/src/ScalarVariable.cpp', 'source/fmipp-code/export/src/SHMManager.cpp', 'source/fmipp-code/export/src/SHMMaster.cpp', 'source/fmipp-code/export/src/SHMSlave.cpp']
import_base_src = ['source/fmipp-code/import/base/src/BareFMU.cpp', 'source/fmipp-code/import/base/src/CallbackFunctions.cpp', 'source/fmipp-code/import/base/src/DynamicalSystem.cpp', 'source/fmipp-code/import/base/src/FMUCoSimulation_v1.cpp', 'source/fmipp-code/import/base/src/FMUCoSimulation_v2.cpp', 'source/fmipp-code/import/base/src/FMUModelExchange_v1.cpp', 'source/fmipp-code/import/base/src/FMUModelExchange_v2.cpp', 'source/fmipp-code/import/base/src/LogBuffer.cpp', 'source/fmipp-code/import/base/src/ModelDescription.cpp', 'source/fmipp-code/import/base/src/ModelManager.cpp', 'source/fmipp-code/import/base/src/PathFromUrl.cpp']
import_integrators_src = ['source/fmipp-code/import/integrators/src/Integrator.cpp', 'source/fmipp-code/import/integrators/src/IntegratorStepper.cpp']
import_utility_src = ['source/fmipp-code/import/utility/src/FixedStepSizeFMU.cpp', 'source/fmipp-code/import/utility/src/History.cpp', 'source/fmipp-code/import/utility/src/IncrementalFMU.cpp', 'source/fmipp-code/import/utility/src/InterpolatingFixedStepSizeFMU.cpp', 'source/fmipp-code/import/utility/src/RollbackFMU.cpp', 'source/fmipp-code/import/utility/src/VariableStepSizeFMU.cpp']
all_cpp = export_functions + export_src + import_base_src + import_integrators_src + import_utility_src
libfmippex_i = ['source/fmipp-code/export/swig/libfmippex.i']
libfmippim_i = ['source/fmipp-code/import/swig/libfmippim.i']
libfmipp_fmu_frontendlib_sources = ['source/fmipp-code/export/src/FMIComponentFrontEnd.cpp', 'source/fmipp-code/export/src/FMIComponentFrontEndBase.cpp', 'source/fmipp-code/export/src/IPCLogger.cpp', 'source/fmipp-code/export/src/IPCMasterLogger.cpp', 'source/fmipp-code/export/src/HelperFunctions.cpp','source/fmipp-code/export/src/ScalarVariable.cpp', 'source/fmipp-code/import/base/src/ModelDescription.cpp', 'source/fmipp-code/import/base/src/PathFromUrl.cpp']
fmi2dll_sources = ['source/fmipp-code/export/functions/fmi_v2.0/fmi2Functions.cpp', 'source/fmipp-code/export/src/ScalarVariable.cpp', 'source/fmipp-code/export/src/FMIComponentFrontEnd.cpp', 'source/fmipp-code/export/src/FMIComponentFrontEndBase.cpp', 'source/fmipp-code/export/src/IPCLogger.cpp', 'source/fmipp-code/export/src/IPCMasterLogger.cpp', 'source/fmipp-code/export/src/SHMMaster.cpp', 'source/fmipp-code/export/src/SHMManager.cpp', 'source/fmipp-code/export/src/HelperFunctions.cpp', 'source/fmipp-code/import/base/src/ModelDescription.cpp', 'source/fmipp-code/import/base/src/PathFromUrl.cpp']
include_directorys = ['source/fmipp-code/', os.path.join(os.path.dirname(__file__),'source','fmipp-code')]
additional_libs = ['boost_filesystem', 'boost_system','sundials_cvode', 'sundials_nvecserial'] 
library_dir = [os.path.join(os.path.dirname(__file__),'fmipp','lib'), os.path.join(os.path.dirname(__file__),'fmipp','export'), os.path.join(os.path.dirname(__file__),'fmipp','export','bin')]
##----------------------------------------------------------------------------------------------------

#Modules------------------------------------------------------------------------------------
if ('win' not in install_platform):
	importpyd =                Extension('fmipp/lib/_fmippim',
										 swig_opts = ['-c++', '-Isource/fmipp-code', '-outdir','fmipp', '-DUSE_SUNDIALS'],
										 sources = libfmippim_i + import_base_src + import_integrators_src + import_utility_src,
										 include_dirs = include_directorys,
										 define_macros = macros,
										 undef_macros = ['NDEBUG'],
										 library_dirs = library_dir,
										 libraries = additional_libs,
										 extra_compile_args = ['-g0','-std=c++11'],
										 extra_link_args = ['-lrt'],
										 runtime_library_dirs = library_dir,
										)
	exportpyd =                Extension('fmipp/export/_fmippex',
										 swig_opts = ['-c++', '-Isource/fmipp-code', '-outdir','fmipp/export', '-DUSE_SUNDIALS'],
										 sources = libfmippex_i + all_cpp,
										 include_dirs = include_directorys,
										 define_macros = macros,
										 undef_macros = ['NDEBUG'],
										 library_dirs = library_dir,
										 libraries = additional_libs,
										 extra_compile_args = ['-g0','-std=c++11'],
										 extra_link_args = ['-lrt'],
										 runtime_library_dirs = library_dir,
										)
	importdll =                Extension('fmipp/lib/libfmippim',
										 sources = import_base_src + import_integrators_src + import_utility_src,
										 include_dirs = include_directorys,
										 define_macros = macros,
										 undef_macros = ['NDEBUG'],
										 extra_compile_args = ['-g0','-std=c++11'],
										 extra_link_args = ['-lrt'],
										 runtime_library_dirs = library_dir,
										)
	exportdll =                Extension('fmipp/lib/libfmippex',
										 sources = export_src,
										 include_dirs = include_directorys,
										 define_macros = macros,
										 undef_macros = ['NDEBUG'],
										 extra_compile_args = ['-g0','-std=c++11'],
										 extra_link_args = ['-lrt'],
										 runtime_library_dirs = library_dir,
										)

	fmi2dll =                  Extension('fmipp/export/bin/libfmi2',
										 sources = fmi2dll_sources,
										 include_dirs = include_directorys,
										 define_macros = macros,
										 undef_macros = ['NDEBUG'],
										 library_dirs = library_dir,
										 libraries = additional_libs,
										 extra_compile_args = ['-g0','-std=c++11'],
										 extra_link_args = ['-lrt'],
										 runtime_library_dirs = library_dir,
										)
	libfmipp_fmu_frontendlib = Extension('fmipp/export/bin/libfmipp_fmu_frontend',
										 sources = libfmipp_fmu_frontendlib_sources,
										 include_dirs = include_directorys + os.getenv('Path',default='').split(os.pathsep),
										 define_macros = macros,
										 undef_macros = ['NDEBUG'],
										 extra_compile_args = ['-g0','-std=c++11'],
										 extra_link_args = ['-lrt'],
										 runtime_library_dirs = library_dir,
										)
##------------------------------------------------------------------------------------------


#Windows specific definitions---------------
# List of additional files (i.e., files without the '.py' extension) that are part of the distribution.
pyfmipp_additional_files = [
  'lib/_fmippim.pyd',
  'lib/_fmippex.pyd',
  'lib/fmippim.dll',
  'lib/fmippex.dll',
  'lib/sundials_cvode.lib',
  'lib/sundials_nvecserial.lib',
  'licenses/FMIPP_LICENSE.txt',
  'licenses/BOOST_SOFTWARE_LICENSE.txt',
  'licenses/SUNDIALS_LICENSE.txt',
  'export/bin/fmi2.dll',
  'export/bin/libfmipp_fmu_frontend.lib',
  'lib/boost_filesystem-vc141-mt-1_64.dll',
  'lib/boost_system-vc141-mt-1_64.dll'
  ]
##------------------------------------------

# Read long description from file (reStructuredText syntax). Will be parsed and displayed as HTML online.
with open( 'description.txt' ) as file: pyfmipp_long_description = file.read()


##### SETUP ##### ------------------------------------------------------------------------------------------
_name = 'fmipp'
_version = '1.4'
_description = 'FMI++ Python Interface for Windows'
_long_description = 'This package provides a Python wrapper for the FMI++ library, which \nintends to bridge the gap between the basic fuctionality provided by \nthe FMI                specification and the typical requirements of simulation tools.'
_url = 'http://fmipp.sourceforge.net'
_maintainer = 'Edmund Widl'
_maintainer_email = 'edmund.widl@ait.ac.at'
_license = 'BSD license & BOOST software license'
_platforms = 'Windows'
_keywords = [ 'FMI', 'Functional Mock-up Interface', 'FMI++ Library' ]
_classifiers = [
         'Development Status :: 4 - Beta',
         'Intended Audience :: Science/Research',
         'Operating System :: Microsoft :: Windows',
         'Operating System :: POSIX :: Linux',
         'Topic :: Scientific/Engineering',
         'Programming Language :: Python :: 3.5',
         'Programming Language :: C++',
        ]
_packages = ['fmipp', 'fmipp.export']



if use_win_wheels:
  setup(name = _name,
        version = _version,
        description = _description,
        #long_description = _long_description,
        long_description = pyfmipp_long_description,
        url = _url,
        maintainer = _maintainer,
        maintainer_email = _maintainer_email,
        license = 'BSD license & BOOST software license',
        platforms = _platforms,
        keywords = _keywords,
        classifiers = _classifiers,
        packages = _packages,
        package_data = { 'fmipp': pyfmipp_additional_files },
        include_package_data=True,
        distclass=BinaryDistribution,
       )
else: #for linux
  setup(name = _name,
      version = _version,
      description = _description,
      #long_description = _long_description,
      long_description = pyfmipp_long_description,
      url = _url,
      maintainer = _maintainer,
      maintainer_email = _maintainer_email,
      license = 'BSD license & BOOST software license',
      platforms = _platforms,
      keywords = _keywords,
      classifiers = _classifiers,
      cmdclass = {'build': CustomBuild},
      packages = _packages,
      ext_modules = [importpyd, exportpyd, importdll, exportdll, fmi2dll, libfmipp_fmu_frontendlib],
     )
