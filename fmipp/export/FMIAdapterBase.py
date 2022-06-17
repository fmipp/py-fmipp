# -----------------------------------------------------------------
# Copyright (c) 2022, AIT Austrian Institute of Technology GmbH.
# All rights reserved. See file FMIPP_LICENSE.txt for details.
# -----------------------------------------------------------------

import warnings
import fmipp.export.fmippex as fmippex
import sys

import abc
try:
	import abc.ABC as ABC
except:
	pass

try:
	from abc import ABCMeta
	class ABC:
		__metaclass__ = ABCMeta
except:
	pass


class FMIAdapterBase( ABC ):
	"""
	Base class for FMI adapter implementations.
	"""

	@abc.abstractmethod
	def init( self, currentCommunicationPoint ):
		"""
		Initialize the FMU (definition of input/output variables and parameters, enforce step size).
		:param currentCommunicationPoint: current communication point of the master algorithm during initialization (float)
		"""
		pass


	@abc.abstractmethod
	def doStep( self, currentCommunicationPoint, communicationStepSize ):
		"""
		Make a simulation step.
		:param currentCommunicationPoint: current communication point of the master algorithm (float)
		:param communicationStepSize: communication step size (float)
		"""
		pass


	@abc.abstractmethod
	def defineRealParameters( self, *parameterNames ):
		"""
		Define parameters (of type real).
		:param *parameterNames: names of parameters of type real
		"""
		pass


	@abc.abstractmethod
	def defineIntegerParameters( self, *parameterNames ):
		"""
		Define parameters (of type integer).
		:param *parameterNames: names of parameters of type integer
		"""
		pass


	@abc.abstractmethod
	def defineBooleanParameters( self, *parameterNames ):
		"""
		Define parameters (of type boolean).
		:param *parameterNames: names of parameters of type boolean
		"""
		pass


	@abc.abstractmethod
	def defineStringParameters( self, *parameterNames ):
		"""
		Define parameters (of type string).
		:param *parameterNames: names of parameters of type string
		"""
		pass


	@abc.abstractmethod
	def defineRealInputs( self, *inputVariableNames ):
		"""
		Define input variables (of type real).
		:param *inputVariableNames: names of input variables of type real
		"""
		pass


	@abc.abstractmethod
	def defineIntegerInputs( self, *inputVariableNames ):
		"""
		Define input variables (of type integer).
		:param *inputVariableNames: names of input variables of type integer
		"""
		pass


	@abc.abstractmethod
	def defineBooleanInputs( self, *inputVariableNames ):
		"""
		Define input variables (of type boolean).
		:param *inputVariableNames: names of input variables of type boolean
		"""
		pass


	@abc.abstractmethod
	def defineStringInputs( self, *inputVariableNames ):
		"""
		Define input variables (of type string).
		:param *inputVariableNames: names of input variables of type string
		"""
		pass


	@abc.abstractmethod
	def defineRealOutputs( self, *outputVariableNames ):
		"""
		Define output variables (of type real).
		:param *outputVariableNames: names of output variables of type real
		"""
		pass


	@abc.abstractmethod
	def defineIntegerOutputs( self, *outputVariableNames ):
		"""
		Define output variables (of type integer).
		:param *outputVariableNames: names of output variables of type integer
		"""
		pass


	@abc.abstractmethod
	def defineBooleanOutputs( self, *outputVariableNames ):
		"""
		Define output variables (of type boolean).
		:param *outputVariableNames: names of output variables of type boolean
		"""
		pass


	@abc.abstractmethod
	def defineStringOutputs( self, *outputVariableNames ):
		"""
		Define output variables (of type string).
		:param *outputVariableNames: names of output variables of type string
		"""
		pass


	@abc.abstractmethod
	def getRealParameterValues( self ):
		"""
		Retrieve parameters (of type real).
		:return: dict of parameters of type real (includes all parameters of type real previously defined during the initialization)
		"""
		pass


	@abc.abstractmethod
	def getIntegerParameterValues( self ):
		"""
		Retrieve parameters (of type integer).
		:return: dict of parameters of type integer (includes all parameters of type integer previously defined during the initialization)
		"""
		pass


	@abc.abstractmethod
	def getBooleanParameterValues( self ):
		"""
		Retrieve parameters (of type boolean).
		:return: dict of parameters of type boolean (includes all parameters of type boolean previously defined during the initialization)
		"""
		pass


	@abc.abstractmethod
	def getStringParameterValues( self ):
		"""
		Retrieve parameters (of type string).
		:return: dict of parameters of type string (includes all parameters of type string previously defined during the initialization)
		"""
		pass


	@abc.abstractmethod
	def getRealInputValues( self ):
		"""
		Retrieve input variables (of type real).
		:return: dict of input variables of type real (includes all input variables of type real previously defined during the initialization)
		"""
		pass


	@abc.abstractmethod
	def getIntegerInputValues( self ):
		"""
		Retrieve input variables (of type integer).
		:return: dict of input variables of type real (includes all input variables of type real previously defined during the initialization)
		"""
		pass


	@abc.abstractmethod
	def getBooleanInputValues( self ):
		"""
		Retrieve input variables (of type boolean).
		:return: dict of input variables of type boolean (includes all input variables of type boolean previously defined during the initialization)
		"""
		pass


	@abc.abstractmethod
	def getStringInputValues( self ):
		"""
		Retrieve input variables (of type string).
		:return: dict of input variables of type string (includes all input variables of type string previously defined during the initialization)
		"""
		pass


	@abc.abstractmethod
	def setRealOutputValues( self, outputValues ):
		"""
		Set output variables (of type real).
		:param outputValues: dict of output variables of type real (must include all output variables of type real previously defined during the initialization)
		"""
		pass


	@abc.abstractmethod
	def setIntegerOutputValues( self, outputValues ):
		"""
		Set output variables (of type integer).
		:param outputValues: dict of output variables of type integer (must include all output variables of type integer previously defined during the initialization)
		"""
		pass


	@abc.abstractmethod
	def setBooleanOutputValues( self, outputValues ):
		"""
		Set output variables (of type boolean).
		:param outputValues: dict of output variables of type boolean (must include all output variables of type boolean previously defined during the initialization)
		"""
		pass


	@abc.abstractmethod
	def setStringOutputValues( self, outputValues ):
		"""
		Set output variables (of type string).
		:param outputValues: dict of output variables of type string (must include all output variables of type string previously defined during the initialization)
		"""
		pass


	def __init__( self ):
		""" Constructor."""
		# This flag indicates whether the FMI export interface is activated.
		self._fmippexActive = False

		# FMI component backend.
		self._backend = None

		# Flag to indicate that a fixed step size is to be enforced.
		self._enforceTimeStep = False

		# Enforced step size.
		self._enforcedTimeStepSize = float( 'NAN' )

		# Real parameters.
		self._realParameters = None
		self._realParameterSize = 0
		self._realParameterNames = []
		self._debugRealParameterValues = []

		# Real input variables.
		self._realInputs = None
		self._realInputSize = 0
		self._realInputNames = []
		self._debugRealInputValues = []

		# Real output variables.
		self._realOutputs = None
		self._realOutputSize = 0
		self._realOutputNames = []
		self._debugRealOutputValues = []

		# Integer parameters.
		self._integerParameters = None
		self._integerParameterSize = 0
		self._integerParameterNames = []
		self._debugIntegerParameterValues = []

		# Integer input variables.
		self._integerInputs = None
		self._integerInputSize = 0
		self._integerInputNames = []
		self._debugIntegerInputValues = []

		# Integer output variables.
		self._integerOutputs = None
		self._integerOutputSize = 0
		self._integerOutputNames = []
		self._debugIntegerOutputValues = []

		# Boolean parameters.
		self._booleanParameters = None
		self._booleanParameterSize = 0
		self._booleanParameterNames = []
		self._debugBooleanParameterValues = []

		# Boolean input variables.
		self._booleanInputs = None
		self._booleanInputSize = 0
		self._booleanInputNames = []
		self._debugBooleanInputValues = []

		# Boolean output variables.
		self._booleanOutputs = None
		self._booleanOutputSize = 0
		self._booleanOutputNames = []
		self._debugBooleanOutputValues = []

		# String parameters.
		self._stringParameters = None
		self._stringParameterSize = 0
		self._stringParameterNames = []
		self._debugStringParameterValues = []

		# String input variables.
		self._stringInputs = None
		self._stringInputSize = 0
		self._stringInputNames = []
		self._debugStringInputValues = []

		# String output variables.
		self._stringOutputs = None
		self._stringOutputSize = 0
		self._stringOutputNames = []
		self._debugStringOutputValues = []


	def enforceTimeStep( self, stepSize ):
		"""
		Enforce time step, call from init(...) function.
		:param stepSize: value of the enforced step size (float)
		"""
		self._enforceTimeStep = True
		self._enforcedTimeStepSize = stepSize


	def checkEnforceTimeStep( self ):
		"""Check if fixed time steps are enforced."""
		return self._enforceTimeStep


	def debugSetRealParameterValues( self, realParameterValues ):
		"""
		Set parameters of type real (in debug mode).
		:param realParameterValues: dict of parameters of type real (must include all parameters of type real previously defined during the initialization)
		"""
		# Sanity check: all defined parameters have to be given as input.
		for name in self._realParameterNames:
			if not name in realParameterValues:
				raise RuntimeError( '[FMIAdapter:debugSetRealParameterValues] parameter \'{}\' is missing.'.format( name ) )

		for i in range( 0, self._realParameterSize ):
			self._debugRealParameterValues[i] = realParameterValues[ self._realParameterNames[i] ]


	def debugSetRealInputValues( self, realInputValues ):
		"""
		Set input values of type real (in debug mode).
		:param realInputValues: dict of input variables of type real (must include all input values of type real previously defined during the initialization)
		"""
		# Sanity check: all defined input variables have to be given as input.
		for name in self._realInputNames:
			if not name in realInputValues:
				raise RuntimeError( '[FMIAdapter:debugSetRealInputValues] input variable \'{}\' is missing.'.format( name ) )

		for i in range( 0, self._realInputSize ):
			self._debugRealInputValues[i] = realInputValues[ self._realInputNames[i] ]


	def debugGetRealOutputValues( self ):
		"""
		Get output values of type real (in debug mode).
		:return: dict of output variables of type real (includes all output variables of type real previously defined during the initialization)
		"""
		debugRealOutputs = {}

		for i in range( 0, self._realOutputSize ):
			debugRealOutputs[ self._realOutputNames[i] ] = self._debugRealOutputValues[i]

		return debugRealOutputs


	def debugSetIntegerParameterValues( self, integerParameterValues ):
		"""
		Set parameters of type integer (in debug mode).
		:param integerParameterValues: dict of parameters of type integer (must include all parameters of type integer previously defined during the initialization)
		"""
		# Sanity check: all defined parameters have to be given as input.
		for name in self._integerParameterNames:
			if not name in integerParameterValues:
				raise RuntimeError( '[FMIAdapter:debugSetIntegerParameterValues] parameter \'{}\' is missing.'.format( name ) )

		for i in range( 0, self._integerParameterSize ):
			self._debugIntegerParameterValues[i] = integerParameterValues[ self._integerParameterNames[i] ]


	def debugSetIntegerInputValues( self, integerInputValues ):
		"""
		Set input values of type integer (in debug mode).
		:param integerInputValues: dict of input variables of type integer (must include all input variables of type integer previously defined during the initialization)
		"""
		# Sanity check: all defined input variables have to be given as input.
		for name in self._integerInputNames:
			if not name in integerInputValues:
				raise RuntimeError( '[FMIAdapter:debugSetIntegerInputValues] input variable \'{}\' is missing.'.format( name ) )

		for i in range( 0, self._integerInputSize ):
			self._debugIntegerInputValues[i] = integerInputValues[ self._integerInputNames[i] ]


	def debugGetIntegerOutputValues( self ):
		"""
		Get output values of type integer (in debug mode).
		:return: dict of output variables of type integer (includes all output variables of type integer previously defined during the initialization)
		"""
		debugIntegerOutputs = {}

		for i in range( 0, self._integerOutputSize ):
			debugIntegerOutputs[ self._integerOutputNames[i] ] = self._debugIntegerOutputValues[i]

		return debugIntegerOutputs


	def debugSetBooleanParameterValues( self, booleanParameterValues ):
		"""
		Set parameters of type boolean (in debug mode).
		:param booleanParameterValues: dict of parameters of type boolean (must include all parameters of type boolean previously defined during the initialization)
		"""
		# Sanity check: all defined parameters have to be given as input.
		for name in self._booleanParameterNames:
			if not name in booleanParameterValues:
				raise RuntimeError( '[FMIAdapter:debugSetBooleanParameterValues] parameter \'{}\' is missing.'.format( name ) )

		for i in range( 0, self._booleanParameterSize ):
			self._debugBooleanParameterValues[i] = booleanParameterValues[ self._booleanParameterNames[i] ]


	def debugSetBooleanInputValues( self, booleanInputValues ):
		"""
		Set input values of type boolean (in debug mode).
		:param booleanInputValues: dict of input variables of type boolean (must include all input variables of type boolean previously defined during the initialization)
		"""
		# Sanity check: all defined input variables have to be given as input.
		for name in self._booleanInputNames:
			if not name in booleanInputValues:
				raise RuntimeError( '[FMIAdapter:debugSetBooleanInputValues] input variable \'{}\' is missing.'.format( name ) )

		for i in range( 0, self._booleanInputSize ):
			self._debugBooleanInputValues[i] = booleanInputValues[ self._booleanInputNames[i] ]


	def debugGetBooleanOutputValues( self ):
		"""
		Get output values of type boolean (in debug mode).
		:return: dict of output variables of type boolean (includes all output variables of type boolean previously defined during the initialization)
		"""
		debugBooleanOutputs = {}

		for i in range( 0, self._booleanOutputSize ):
			debugBooleanOutputs[ self._booleanOutputNames[i] ] = self._debugBooleanOutputValues[i]

		return debugBooleanOutputs


	def debugSetStringParameterValues( self, stringParameterValues ):
		"""
		Set parameters of type string (in debug mode).
		:param stringParameterValues: dict of parameters of type string (must include all parameters of type string previously defined during the initialization)
		"""
		# Sanity check: all defined parameters have to be given as input.
		for name in self._stringParameterNames:
			if not name in stringParameterValues:
				raise RuntimeError( '[FMIAdapter:debugSetStringParameterValues] parameter \'{}\' is missing.'.format( name ) )

		for i in range( 0, self._stringParameterSize ):
			self._debugStringParameterValues[i] = stringParameterValues[ self._stringParameterNames[i] ]


	def debugSetStringInputValues( self, stringInputValues ):
		"""
		Set input values of type string (in debug mode).
		:param stringInputValues: dict of input variables of type string (must include all input variables of type string previously defined during the initialization)
		"""
		# Sanity check: all defined input variables have to be given as input.
		for name in self._stringInputNames:
			if not name in stringInputValues:
				raise RuntimeError( '[FMIAdapter:debugSetStringInputValues] input variable \'{}\' is missing.'.format( name ) )

		for i in range( 0, self._stringInputSize ):
			self._debugStringInputValues[i] = stringInputValues[ self._stringInputNames[i] ]


	def debugGetStringOutputValues( self ):
		"""
		Get output values of type string (in debug mode).
		:return: dict of output variables of type string (includes all output variables of type string previously defined during the initialization)
		"""
		debugStringOutputs = {}

		for i in range( 0, self._stringOutputSize ):
			debugStringOutputs[ self._stringOutputNames[i] ] = self._debugStringOutputValues[i]

		return debugStringOutputs


	def _defineVariables( self, names, size, variables, type, debugValues, funcInitParams ):
		"""Generic function for the definition of variables (inputs, outputs, parameters)"""
		# Check if export interface is active.
		if self._fmippexActive is False:
			warnings.warn( 'FMI++ export interface is not active.', RuntimeWarning )
			try:
				debugValues.clear()
			except:
				while len(debugValues) > 0 : debugValues.pop()
			debugValues.extend( [ type() ] * size )
			return fmippex.fmi2OK

		# Define variable names.
		labels = fmippex.new_string_array( size )
		for i in range( 0, size ): fmippex.string_array_setitem( labels, i, names[i] )

		# Initialize variables.
		return funcInitParams( labels, variables, size )


	def _getValues( self, names, size, variables, type, debugValues, funcGetValues, funcGetItem ):
		"""Generic getter function (inputs, parameters)"""
		# Check if export interface is active.
		if self._fmippexActive is False:
			warnings.warn( 'FMI++ export interface is not active.', RuntimeWarning )
			return dict( [ ( n, v ) for n, v in zip( names, debugValues ) ] )

		# Read parameters.
		status = funcGetValues( variables, size )
		if not status is fmippex.fmi2OK: return None

		getValues = [ type() ] * size
		for i in range( 0, size ): getValues[i] = type( funcGetItem( variables, i ) )
		return dict( [ ( n, v ) for n, v in zip( names, getValues ) ] )


	def _setValues( self, names, size, variables, values, debugValues, funcSetValues, funcSetItem ):
		"""Generic setter function (outputs)"""
		# Check if export interface is active.
		if self._fmippexActive is False:
			warnings.warn( 'FMI++ export interface is not active.', RuntimeWarning )
			try:
				debugValues.clear()
			except:
				while len(debugValues) > 0 : debugValues.pop()
			debugValues.extend( [ values[ name ] for name in names ] )
			return fmippex.fmi2OK

		# Set output values.
		for i in range( 0, size ): funcSetItem( variables, i, values[ names[i] ] )

		# Write current outputs.
		return funcSetValues( variables, size )


	def _initBackEnd( self ):
		"""Initialize base. Call this function in order to activate the FMI export interface during co-simulation."""
		# Variable that indicates if FMI++ export interface is active.
		self._fmippexActive = True

		# Create a new FMI backend.
		self._backend = fmippex.FMIComponentBackEnd()

		# Start the initialization of the backend.
		initStatus = self._backend.startInitialization()
		if not initStatus is fmippex.fmi2OK:
			raise RuntimeError( '[FMIAdapter:initBackEnd] start of initialization of FMI++ interface unsuccessful' )

		self.init( self._backend.getCurrentCommunicationPoint() )

		if self._enforceTimeStep is True:
			# Let's do fixed time steps!
			self._backend.enforceTimeStep( self._enforcedTimeStepSize )

		# End the initialization of the backend.
		initStatus = self._backend.endInitialization()

		if not initStatus is fmippex.fmi2OK:
			raise RuntimeError( '[FMIAdapter:initBackEnd] end of initialization of FMI++ interface unsuccessful' )


	def _run( self ):
		"""Iterate the FMU."""
		while self._fmippexActive is True:
			# Wait for simulation master to hand over control.
			self._backend.waitForMaster()

			# Make a step.
			self.doStep( self._backend.getCurrentCommunicationPoint(), self._backend.getCommunicationStepSize() )

			if self._enforceTimeStep is True:
				# Let's do fixed time steps!
				self._backend.enforceTimeStep( self._enforcedTimeStepSize )

			# Give back control to simulation master.
			self._backend.signalToMaster()
