# -----------------------------------------------------------------
# Copyright (c) 2015, AIT Austrian Institute of Technology GmbH.
# All rights reserved. See file TRNSYS_FMU_LICENSE.txt for details.
# -----------------------------------------------------------------

import os.path
import sys

# Retrieve current path.
install_dir = os.path.dirname( os.path.abspath( __file__ ) )

# Add directory containing the SWIG modules and external libraries.
sys.path.append( os.path.join( install_dir, "lib" ) ) 

# Import the FMI++ wrapper.
from fmippim import *