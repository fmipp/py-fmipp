# -----------------------------------------------------------------
# Copyright (c) 2015, AIT Austrian Institute of Technology GmbH.
# All rights reserved. See file FMIPP_LICENSE.txt for details.
# -----------------------------------------------------------------

'''This module provides a Python interface for the FMI++ Library.'''

import os.path, sys

# Retrieve current path.
install_dir = os.path.dirname( os.path.abspath( __file__ ) )

# Add directory containing the SWIG modules and external libraries.
sys.path.append( os.path.join( install_dir, "lib" ) ) 

# Import FMI++ wrapper.
from .fmippim import *

# Import utility scripts.
from .extractFMU import *
from .pathToURI import *
from .simplifyModelDescription import *

try:
	from .numeric import *
except Exception as ex:
	print( ex )

# Extra info regarding licenses.
def licenseInfo():
	import textwrap

	info1 = 'The FMI++ Python Interface is based on code from the FMI++ Library and BOOST. Also, it includes compiled libraries implementing the SUNDIALS CVODE integrator.'
	info2 = 'For detailed information on the respective licenses please refer to the license files provided here:'

	width = 65
	full_info = '\n{}\n\n{}\n\n{}\n'.format( textwrap.fill( info1, width ), textwrap.fill( info2, width ), os.path.join( install_dir, 'licenses' ) )
	
	print( full_info )
