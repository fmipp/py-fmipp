from distutils.core import setup

additional_files = [
  'lib/_fmippim.pyd',
  'lib/fmippim.dll',
  'lib/sundials_cvode.dll',
  'lib/sundials_nvecserial.dll',
  'licenses/FMIPP_LICENSE.txt',
  'licenses/SUNDIALS_LICENSE.txt'
  ]

setup(
  name =' fmipp',
  version = '0.1',
  description = 'FMI++ Python Wrapper (Windows 32-bit)',
  long_description = 'This package provides a Python wrapper for the FMI++ library, which \nintends to bridge the gap between the basic fuctionality provided by \nthe FMI specification and the typical requirements of simulation tools.',
  author = 'Edmund Widl <edmund.widl@ait.ac.at>, \n\tWolfgang Mueller <wolfgang.mueller.fl@ait.ac.at>',
  maintainer = 'Edmund Widl',
  maintainer_email = 'edmund.widl@ait.ac.at',
  license = 'BSD (see FMIPP_LICENSE.txt and SUNDIALS_LICENSE.txt)',
  platforms = 'Windows',
  classifiers=[
    'Development Status :: 4 - Beta',
	'Intended Audience :: End Users/Desktop',
	'Intended Audience :: Science/Research',
	'License :: OSI Approved :: BSD License',
	'Operating System :: Microsoft :: Windows',
	'Topic :: Scientific/Engineering'
	'Programming Language :: Python',
	],
  packages = [ 'fmipp' ],
  package_data = { 'fmipp': additional_files },
  )