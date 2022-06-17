# -----------------------------------------------------------------
# Copyright (c) 2022, AIT Austrian Institute of Technology GmbH.
# All rights reserved. See file FMIPP_LICENSE.txt for details.
# -----------------------------------------------------------------

'''This module provides a Python interface for the FMI++ Library.'''

import os.path, sys

# Retrieve current path.
install_dir = os.path.dirname( os.path.abspath( __file__ ) )

# Add directory containing the SWIG modules and external libraries.
sys.path.append( os.path.join( install_dir ) )

# Import FMI++ wrapper.
from .fmippex import *
