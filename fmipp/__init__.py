# -----------------------------------------------------------------
# Copyright (c) 2015, AIT Austrian Institute of Technology GmbH.
# All rights reserved. See file FMIPP_LICENSE.txt for details.
# -----------------------------------------------------------------

"""This module provides a Python Interface for the FMI++ Library."""

import os.path, sys, imp, glob

# Retrieve current path.
install_dir = os.path.dirname( os.path.abspath( __file__ ) )

# Add directory containing the SWIG modules and external libraries.
sys.path.append( os.path.join( install_dir, "lib" ) ) 

# Import additional FMI++ scripts.
scripts = glob.glob( os.path.join( install_dir, "*.py" ) )
for s in scripts:

	path, fname = os.path.split( s )
	mname, ext = os.path.splitext( fname )

	if mname not in [ '__init__' ]:
		no_ext = os.path.join( path, mname )

		if os.path.exists( no_ext + '.py' ):
			try:
				imp.load_source( 'fmipp', no_ext + '.py' )
				#print 'successfully loaded module %s' % mname
			except:
				print( 'failed loading module %s' % mname )
				print( sys.exc_info()[0] )


# Extra info regarding licenses.
def licenseInfo():
	import textwrap

	info1 = 'The FMI++ Python Interface for Windows is based on code from the FMI++ Library and BOOST. Also, it includes compiled libraries implementing the SUNDIALS CVODE integrator.'
	info2 = 'For detailed information on the respective licenses please refer to the license files provided here:'

	width = 65
	full_info = '\n{}\n\n{}\n\n{}\n'.format( textwrap.fill( info1, width ), textwrap.fill( info2, width ), os.path.join( install_dir, 'licenses' ) )
	
	print( full_info )
