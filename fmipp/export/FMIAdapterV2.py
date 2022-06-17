# -----------------------------------------------------------------
# Copyright (c) 2022, AIT Austrian Institute of Technology GmbH.
# All rights reserved. See file FMIPP_LICENSE.txt for details.
# -----------------------------------------------------------------

import abc
import warnings
import fmipp.export.fmippex as fmippex
from fmipp.export.FMIAdapterBase import FMIAdapterBase


class FMIAdapterV2( FMIAdapterBase ):
    """
    Abtract base class for defining FMUs for Co-Simulation compliant to FMI version 2.0.
    To implement an FMU, inherit a new class from class FMIAdapter that implements the methods init(...) and doStep(...).
    This class is a user-friendly wrapper for the functionality provided by the SWIG-generated Python bindings of the FMI++ library.
    """

    def defineRealParameters( self, *parameterNames ):
        """
        Define parameters (of type real).
        :param *parameterNames: names of parameters of type real
        """
        self._realParameterNames = list( parameterNames )
        self._realParameterSize = len( self._realParameterNames )
        self._realParameters = fmippex.new_double_array( self._realParameterSize )

        # Initialize parameters of type real.
        status = self._defineVariables(
            self._realParameterNames, self._realParameterSize,
            self._realParameters, float, self._debugRealParameterValues, 
            self._backend.initializeRealParameters if not self._backend is None else None )

        if not status is fmippex.fmi2OK:
            raise RuntimeError( '[FMIAdapter:defineRealParameters] initializeRealParameters not successful' )
    

    def defineRealInputs( self, *inputVariableNames ):
        """
        Define input variables (of type real).
        :param *inputVariableNames: names of input variables of type real
        """
        self._realInputNames = list( inputVariableNames )
        self._realInputSize = len( self._realInputNames )
        self._realInputs = fmippex.new_double_array( self._realInputSize )

        # Initialize inputs (of type real).
        status = self._defineVariables(
            self._realInputNames, self._realInputSize,
            self._realInputs, float, self._debugRealInputValues, 
            self._backend.initializeRealInputs if not self._backend is None else None )

        if not status is fmippex.fmi2OK:
            raise RuntimeError( '[FMIAdapter:defineRealInputs] initializeRealInputs not successful' )


    def defineRealOutputs( self, *outputVariableNames ):
        """
        Define output variables (of type real).
        :param *outputVariableNames: names of output variables of type real
        """
        self._realOutputNames = list( outputVariableNames )
        self._realOutputSize = len( self._realOutputNames )
        self._realOutputs = fmippex.new_double_array( self._realOutputSize )

        # Initialize outputs (of type real).
        status = self._defineVariables(
            self._realOutputNames, self._realOutputSize,
            self._realOutputs, float, self._debugRealOutputValues, 
            self._backend.initializeRealOutputs if not self._backend is None else None )

        if not status is fmippex.fmi2OK:
            raise RuntimeError( '[FMIAdapter:defineRealOutputs] initializeRealOutputs not successful' ); end


    def defineIntegerParameters( self, *parameterNames ):
        """
        Define parameters (of type integer).        
        :param *parameterNames: names of parameters of type integer
        """
        self._integerParameterNames = list( parameterNames )
        self._integerParameterSize = len( self._integerParameterNames )
        self._integerParameters = fmippex.new_int_array( self._integerParameterSize )

        # Initialize parameters of type integer.
        status = self._defineVariables(
            self._integerParameterNames, self._integerParameterSize,
            self._integerParameters, int, self._debugIntegerParameterValues, 
            self._backend.initializeIntegerParameters if not self._backend is None else None )

        if not status is fmippex.fmi2OK:
            raise RuntimeError( '[FMIAdapter:defineIntegerParameters] initializeIntegerParameters not successful' )


    def defineIntegerInputs( self, *inputVariableNames ):
        """
        Define input variables (of type integer).
        :param *inputVariableNames: names of input variables of type integer
        """
        self._integerInputNames = list( inputVariableNames )
        self._integerInputSize = len( self._integerInputNames )
        self._integerInputs = fmippex.new_int_array( self._integerInputSize )

        # Initialize inputs (of type integer).
        status = self._defineVariables(
            self._integerInputNames, self._integerInputSize,
            self._integerInputs, int, self._debugIntegerInputValues, 
            self._backend.initializeIntegerInputs if not self._backend is None else None )

        if not status is fmippex.fmi2OK:
            raise RuntimeError( '[FMIAdapter:defineIntegerInputs] initializeIntegerInputs not successful' )


    def defineIntegerOutputs( self, *outputVariableNames ):
        """
        Define output variables (of type integer).
        :param *outputVariableNames: names of output variables of type integer
        """
        self._integerOutputNames = list( outputVariableNames )
        self._integerOutputSize = len( self._integerOutputNames )
        self._integerOutputs = fmippex.new_int_array( self._integerOutputSize )

        # Initialize outputs (of type integer).
        status = self._defineVariables(
            self._integerOutputNames, self._integerOutputSize,
            self._integerOutputs, int, self._debugIntegerOutputValues, 
            self._backend.initializeIntegerOutputs if not self._backend is None else None )

        if not status is fmippex.fmi2OK:
            raise RuntimeError( '[FMIAdapter:defineIntegerOutputs] initializeIntegerOutputs not successful' )


    def defineBooleanParameters( self, *parameterNames ):
        """
        Define parameters (of type boolean).        
        :param *parameterNames: names of parameters of type boolean
        """
        self._booleanParameterNames = list( parameterNames )
        self._booleanParameterSize = len( self._booleanParameterNames )
        self._booleanParameters = fmippex.new_bool_array( self._booleanParameterSize )

        # Initialize parameters of type boolean.
        status = self._defineVariables(
            self._booleanParameterNames, self._booleanParameterSize,
            self._booleanParameters, bool, self._debugBooleanParameterValues, 
            self._backend.initializeBooleanParameters if not self._backend is None else None )

        if not status is fmippex.fmi2OK:
            raise RuntimeError( '[FMIAdapter:defineBooleanParameters] initializeBooleanParameters not successful' )


    def defineBooleanInputs( self, *inputVariableNames ):
        """
        Define input variables (of type boolean).
        :param *inputVariableNames: names of input variables of type boolean
        """
        self._booleanInputNames = list( inputVariableNames )
        self._booleanInputSize = len( self._booleanInputNames )
        self._booleanInputs = fmippex.new_bool_array( self._booleanInputSize )

        # Initialize inputs (of type boolean).
        status = self._defineVariables(
            self._booleanInputNames, self._booleanInputSize,
            self._booleanInputs, bool, self._debugBooleanInputValues, 
            self._backend.initializeBooleanInputs if not self._backend is None else None )

        if not status is fmippex.fmi2OK:
            raise RuntimeError( '[FMIAdapter:defineBooleanInputs] initializeBooleanInputs not successful' )


    def defineBooleanOutputs( self, *outputVariableNames ):
        """
        Define output variables (of type boolean).
        :param *outputVariableNames: names of output variables of type boolean
        """
        self._booleanOutputNames = list( outputVariableNames )
        self._booleanOutputSize = len( self._booleanOutputNames )
        self._booleanOutputs = fmippex.new_bool_array( self._booleanOutputSize )

        # Initialize outputs (of type boolean).
        status = self._defineVariables(
            self._booleanOutputNames, self._booleanOutputSize,
            self._booleanOutputs, bool, self._debugBooleanOutputValues, 
            self._backend.initializeBooleanOutputs if not self._backend is None else None )

        if not status is fmippex.fmi2OK:
            raise RuntimeError( '[FMIAdapter:defineBooleanOutputs] initializeBooleanOutputs not successful' )


    def defineStringParameters( self, *parameterNames ):
        """
        Define Parameters (of type string).        
        :param *parameterNames: names of parameters of type string
        """
        self._stringParameterNames = list( parameterNames )
        self._stringParameterSize = len( self._stringParameterNames )
        self._stringParameters = fmippex.new_string_array( self._stringParameterSize )

        # Initialize parameters of type string.
        status = self._defineVariables(
            self._stringParameterNames, self._stringParameterSize,
            self._stringParameters, str, self._debugStringParameterValues, 
            self._backend.initializeStringParameters if not self._backend is None else None )

        if not status is fmippex.fmi2OK:
            raise RuntimeError( '[FMIAdapter:defineStringParameters] initializeStringParameters not successful' )


    def defineStringInputs( self, *inputVariableNames ):
        """
        Define input variables (of type string).
        :param *inputVariableNames: names of input variables of type boolean
        """
        self._stringInputNames = list( inputVariableNames )
        self._stringInputSize = len( self._stringInputNames )
        self._stringInputs = fmippex.new_string_array( self._stringInputSize )

        # Initialize inputs (of type string).
        status = self._defineVariables(
            self._stringInputNames, self._stringInputSize,
            self._stringInputs, str, self._debugStringInputValues, 
            self._backend.initializeStringInputs if not self._backend is None else None )

        if not status is fmippex.fmi2OK:
            raise RuntimeError( 'FMIAdapter:defineStringInputs] initializeStringInputs not successful' )


    def defineStringOutputs( self, *outputVariableNames ):
        """
        Define output variables (of type string).
        :param *outputVariableNames: names of output variables of type string
        """
        self._stringOutputNames = list( outputVariableNames )
        self._stringOutputSize = len( self._stringOutputNames )
        self._stringOutputs = fmippex.new_string_array( self._stringOutputSize )

        # Initialize outputs (of type string).
        status = self._defineVariables(
            self._stringOutputNames, self._stringOutputSize,
            self._stringOutputs, str, self._debugStringOutputValues, 
            self._backend.initializeStringOutputs if not self._backend is None else None )

        if not status is fmippex.fmi2OK:
            raise RuntimeError( '[FMIAdapter:defineStringOutputs] initializeStringOutputs not successful' )


    def getRealParameterValues( self ):
        """
        Retrieve parameters (of type real).
        :return: dict of parameters of type real (includes all parameters of type real previously defined during the initialization)
        """
        # Read real parameters.
        values = self._getValues(
            self._realParameterNames, self._realParameterSize,
            self._realParameters, float, self._debugRealParameterValues,
            self._backend.getRealParameters if not self._backend is None else None,
            fmippex.double_array_getitem )
        
        if values is None:
            raise RuntimeError( '[FMIAdapter:getRealParameterValues] getRealParameters not successful' )

        return values
        
        
    def getIntegerParameterValues( self ):
        """
        Retrieve parameters (of type integer).
        :return: dict of parameters of type integer (includes all parameters of type integer previously defined during the initialization)
        """
        # Read integer parameters.
        values = self._getValues(
            self._integerParameterNames, self._integerParameterSize,
            self._integerParameters, int, self._debugIntegerParameterValues,
            self._backend.getIntegerParameters if not self._backend is None else None,
            fmippex.int_array_getitem )
        
        if values is None:
            raise RuntimeError( '[FMIAdapter:getIntegerParameterValues] getIntegerParameterValues not successful' )

        return values


    def getBooleanParameterValues( self ):
        """
        Retrieve parameters (of type boolean).
        :return: dict of parameters of type boolean (includes all parameters of type boolean previously defined during the initialization)
        """
        # Read boolean parameters.
        values = self._getValues(
            self._booleanParameterNames, self._booleanParameterSize,
            self._booleanParameters, bool, self._debugBooleanParameterValues,
            self._backend.getBooleanParameters if not self._backend is None else None,
            fmippex.bool_array_getitem )
        
        if values is None:
            raise RuntimeError( '[FMIAdapter:getBooleanParameterValues] getBooleanParameterValues not successful' )

        return values


    def getStringParameterValues( self ):
        """
        Retrieve parameters (of type string).
        :return: dict of parameters of type string (includes all parameters of type string previously defined during the initialization)
        """
        # Read string parameters.
        values = self._getValues(
            self._stringParameterNames, self._stringParameterSize,
            self._stringParameters, str, self._debugStringParameterValues,
            self._backend.getStringParameters if not self._backend is None else None,
            fmippex.string_array_getitem )
        
        if values is None:
            raise RuntimeError( '[FMIAdapter:getStringParameterValues] getStringParameterValues not successful' )

        return values


    def getRealInputValues( self ):
        """
        Retrieve input variables (of type real).
        :return: dict of input variables of type real (includes all input variables of type real previously defined during the initialization)
        """
        # Read real inputs.
        values = self._getValues(
            self._realInputNames, self._realInputSize,
            self._realInputs, float, self._debugRealInputValues,
            self._backend.getRealInputs if not self._backend is None else None,
            fmippex.double_array_getitem )
        
        if values is None:
            raise RuntimeError( '[FMIAdapter:getRealInputValues] getRealInputValues not successful' )

        return values


    def getIntegerInputValues( self ):
        """
        Retrieve input variables (of type integer).
        :return: dict of input variables of type integer (includes all input variables of type integer previously defined during the initialization)
        """
        # Read integer inputs.
        values = self._getValues(
            self._integerInputNames, self._integerInputSize,
            self._integerInputs, int, self._debugIntegerInputValues,
            self._backend.getIntegerInputs if not self._backend is None else None,
            fmippex.int_array_getitem )
        
        if values is None:
            raise RuntimeError( '[FMIAdapter:getIntegerInputValues] getIntegerInputValues not successful' )

        return values


    def getBooleanInputValues( self ):
        """
        Retrieve input variables (of type boolean).
        :return: dict of input variables of type boolean (includes all input variables of type boolean previously defined during the initialization)
        """
        # Read boolean inputs.
        values = self._getValues(
            self._booleanInputNames, self._booleanInputSize,
            self._booleanInputs, bool, self._debugBooleanInputValues,
            self._backend.getBooleanInputs if not self._backend is None else None,
            fmippex.bool_array_getitem )
        
        if values is None:
            raise RuntimeError( '[FMIAdapter:getBooleanInputValues] getBooleanInputValues not successful' )

        return values


    def getStringInputValues( self ):
        """
        Retrieve input variables (of type string).
        :return: dict of input variables of type string (includes all input variables of type string previously defined during the initialization)
        """
        # Read string inputs.
        values = self._getValues(
            self._stringInputNames, self._stringInputSize,
            self._stringInputs, str, self._debugStringInputValues,
            self._backend.getStringInputs if not self._backend is None else None,
            fmippex.string_array_getitem )
        
        if values is None:
            raise RuntimeError( '[FMIAdapter:getStringInputValues] getStringInputValues not successful' )

        return values


    def setRealOutputValues( self, outputValues ):
        """
        Set output variables (of type real).
        :param outputValues: dict of output variables of type real (must include all output variables of type real previously defined during the initialization)
        """
        # Sanity check: all defined output variables have to be given as input.
        for name in self._realOutputNames:
            if not name in outputValues:
                raise RuntimeError( '[FMIAdapter:setRealOutputValues] output variable \'{}\' is missing.'.format( name ) )

        # Write current outputs.
        status = self._setValues( self._realOutputNames, self._realOutputSize, 
            self._realOutputs, outputValues, self._debugRealOutputValues,
            self._backend.setRealOutputs if not self._backend is None else None,
            fmippex.double_array_setitem )

        if not status is fmippex.fmi2OK:
            raise RuntimeError( '[FMIAdapter:setRealOutputValues] setRealOutputs not successful' )
    
    
    def setIntegerOutputValues( self, outputValues ):
        """
        Set output variables (of type integer).
        :param outputValues: dict of output variables of type integer (must include all output variables of type integer previously defined during the initialization)
        """
        # Sanity check: all defined output variables have to be given as input.
        for name in self._integerOutputNames:
            if not name in outputValues:
                raise RuntimeError( '[FMIAdapter:setIntegerOutputValues] output variable \'{}\' is missing.'.format( name ) )

        # Write current outputs.
        status = self._setValues( self._integerOutputNames, self._integerOutputSize,
            self._integerOutputs, outputValues, self._debugIntegerOutputValues,
            self._backend.setIntegerOutputs if not self._backend is None else None,
            fmippex.int_array_setitem )

        if not status is fmippex.fmi2OK:
            raise RuntimeError( '[FMIAdapter:setIntegerOutputValues] setIntegerOutputs not successful' )


    def setBooleanOutputValues( self, outputValues ):
        """
        Set output variables (of type boolean).
        :param outputValues: dict of output variables of type boolean (must include all output variables of type boolean previously defined during the initialization)
        """
        # Sanity check: all defined output variables have to be given as input.
        for name in self._booleanOutputNames:
            if not name in outputValues:
                raise RuntimeError( '[FMIAdapter:setBooleanOutputValues] output variable \'{}\' is missing.'.format( name ) )

        # Write current outputs.
        status = self._setValues( self._booleanOutputNames, self._booleanOutputSize,
            self._booleanOutputs, outputValues, self._debugBooleanOutputValues,
            self._backend.setBooleanOutputs if not self._backend is None else None,
            fmippex.bool_array_setitem )

        if not status is fmippex.fmi2OK:
            raise RuntimeError( '[FMIAdapter:setBooleanOutputValues] setBooleanOutputs not successful' )


    def setStringOutputValues( self, outputValues ):
        """
        Set output variables (of type string). 
        :param outputValues: dict of output variables of type string (must include all output variables of type string previously defined during the initialization)
        """
        # Sanity check: all defined output variables have to be given as input.
        for name in self._stringOutputNames:
            if not name in outputValues:
                raise RuntimeError( '[FMIAdapter:setStringOutputValues] output variable \'{}\' is missing.'.format( name ) )

        # Write current outputs.
        status = self._setValues( self._stringOutputNames, self._stringOutputSize,
            self._stringOutputs, outputValues, self._debugStringOutputValues,
            self._backend.setStringOutputs if not self._backend is None else None,
            fmippex.string_array_setitem )

        if not status is fmippex.fmi2OK:
            raise RuntimeError( '[FMIAdapter:setStringOutputValues] setStringOutputs not successful' )
