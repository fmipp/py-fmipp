# -----------------------------------------------------------------
# Copyright (c) 2022, AIT Austrian Institute of Technology GmbH.
# All rights reserved. See file FMIPP_LICENSE.txt for details.
# -----------------------------------------------------------------

import fmipp
import sys

def runFMUBackend( backend_class_file_path, backend_class_name ):
	"""
	Initialize and run the FMU back-end.

	:param backend_class_file_path: path to file implementing the FMU back-end
	:param backend_class_name: name of class implementing the FMU back-end
	"""
	try:
		import importlib

		# Creating a ModuleSpec instance based on the path to the class file.
		spec = importlib.util.spec_from_file_location( backend_class_name, backend_class_file_path )

		# Load class inside separate module.
		module = importlib.util.module_from_spec( spec )
		spec.loader.exec_module( module )
	except:
		import imp

		module = imp.load_source( backend_class_name, backend_class_file_path )

	# Retrieve class implementing the FMU back-end.
	backend_class = getattr( module, backend_class_name )

	# Instantiate FMU back-end.
	backend = backend_class()

	try:
		# Initialize the FMU back-end.
		backend._initBackEnd()

		# Enter the simulation loop.
		backend._run()
	except Exception as ex:
		print( ex )
