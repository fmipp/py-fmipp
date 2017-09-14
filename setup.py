from distutils.core import setup


# List of additional files (i.e., files without the '.py' extension) that are part of the distribution.
pyfmipp_additional_files = [
  'lib/_fmippim.pyd',
  'lib/fmippim.dll',
  'lib/sundials_cvode.dll',
  'lib/sundials_nvecserial.dll',
  'licenses/FMIPP_LICENSE.txt',
  'licenses/BOOST_SOFTWARE_LICENSE.txt',
  'licenses/SUNDIALS_LICENSE.txt',
  ]

  
# Read long description from file (reStructuredText syntax). Will be parsed and displayed as HTML online.
with open( 'README.txt' ) as file: pyfmipp_long_description = file.read()


# Specify the setup of this package.
setup(
  name = 'fmipp',
  version = '1.2',
  description = 'FMI++ Python Interface for Windows',
  #long_description = 'This package provides a Python wrapper for the FMI++ library, which \nintends to bridge the gap between the basic fuctionality provided by \nthe FMI specification and the typical requirements of simulation tools.',
  long_description = pyfmipp_long_description,
  url = 'http://fmipp.sourceforge.net',
  maintainer = 'Edmund Widl',
  maintainer_email = 'edmund.widl@ait.ac.at',
  license = 'BSD license & BOOST software license',
  platforms = 'Windows',
  keywords = [ 'FMI', 'Functional Mock-up Interface', 'FMI++ Library' ],
  classifiers=[
    'Development Status :: 4 - Beta',
	'Intended Audience :: Science/Research',
	'Operating System :: Microsoft :: Windows',
	'Topic :: Scientific/Engineering',
	'Programming Language :: Python :: 2.7',
	'Programming Language :: Python :: 3.5',
	'Programming Language :: C++',
	],
  packages = [ 'fmipp' ],
  package_data = { 'fmipp': pyfmipp_additional_files },
  )
