Class fmipp.export.FMIAdapterBase
=================================

.. py:class:: FMIAdapterBase()

   Base class for FMI adapter implementations.
   Defines abtract methods that must be implemented by inheriting classes.
   See `here <https://github.com/fmipp/py-fmipp-tutorial/blob/master/demos/TestFMUExport.ipynb>`__ and `here <https://github.com/fmipp/py-fmipp-tutorial/blob/master/demos/TestFMUExportDebug.ipynb>`__ for an example of usage.


   .. rubric:: Descendants
      :name: descendants

   -  :doc:`fmipp.export.FMIAdapterV2.FMIAdapterV2 </reference/FMIAdapterV2>`


   .. rubric:: Methods
      :name: methods

   .. py:method:: enforceTimeStep(stepSize)

      Enforce time step, call from ``init(...)`` function.

      :param stepSize: value of the enforced step size (float)

   .. py:method:: checkEnforceTimeStep()

      Check if fixed time steps are enforced.

   .. py:method:: debugSetRealParameterValues(realParameterValues)

      Set parameters of type real (in debug mode):

      :param realParameterValues: dict of parameters of type real (must include all parameters of type real previously defined during the initialization)
      :type realParameterValues: dict[str, float]

   .. py:method:: debugSetRealInputValues(realInputValues)

      Set input values of type real (in debug mode).

      :param realInputValues: dict of input variables of type real (must include all input values of type real previously defined during the initialization)
      :type realInputValues: dict[str, float]

   .. py:method:: debugGetRealOutputValues()

      Get output values of type real (in debug mode).

      :return: dict of output variables of type real (includes all output variables of type real previously defined during the initialization)
      :rtype: dict[str, float]

   .. py:method:: debugSetIntegerParameterValues(integerParameterValues)

      Set parameters of type integer (in debug mode).

      :param integerParameterValues: dict of parameters of type integer (must include all parameters of type integer previously defined during the initialization)
      :type integerParameterValues: dict[str, int]

   .. py:method:: debugSetIntegerInputValues(integerInputValues)

      Set input values of type integer (in debug mode).

      :param integerInputValues: dict of input variables of type integer (must include all input variables of type integer previously defined during the initialization)
      :type integerInputValues: dict[str, int]

   .. py:method:: debugGetIntegerOutputValues()

      Get output values of type integer (in debug mode).

      :return: dict of output variables of type integer (includes all output variables of type integer previously defined during the initialization)
      :rtype: dict[str, int]

   .. py:method:: debugSetBooleanParameterValues(booleanParameterValues)

      Set parameters of type boolean (in debug mode).

      :param booleanParameterValues: dict of parameters of type boolean (must include all parameters of type boolean previously defined during the initialization)
      :type booleanParameterValues: dict[str, bool]

   .. py:method:: debugSetBooleanInputValues(booleanInputValues)

      Set input values of type boolean (in debug mode).

      :param booleanInputValues: dict of input variables of type boolean (must include all input variables of type boolean previously defined during the initialization)
      :type booleanInputValues: dict[str, bool]

   .. py:method:: debugGetBooleanOutputValues()

      Get output values of type boolean (in debug mode).

      :return: dict of output variables of type boolean (includes all output variables of type boolean previously defined during the initialization)
      :rtype: dict[str, bool]

   .. py:method:: debugSetStringParameterValues(stringParameterValues)

      Set parameters of type string (in debug mode).

      :param stringParameterValues: dict of parameters of type string (must include all parameters of type string previously defined during the initialization)
      :type stringParameterValues: dict[str, str]

   .. py:method:: debugSetStringInputValues(stringInputValues)

      Set input values of type string (in debug mode).

      :param stringInputValues: dict of input variables of type string (must include all input variables of type string previously defined during the initialization)
      :type stringInputValues: dict[str, str]

   .. py:method:: debugGetStringOutputValues()

      Get output values of type string (in debug mode).

      :return: dict of output variables of type string (includes all output variables of type string previously defined during the initialization)
      :rtype: dict[str, str]


   .. rubric:: Abstract Methods
      :name: abstract-methods

   .. py:method:: init(currentCommunicationPoint)
      :abstractmethod:

      Initialize the FMU (definition of input/output variables and parameters, enforce step size).

      :param float currentCommunicationPoint: current communication point of the master algorithm during initialization (float)

   .. py:method:: doStep(currentCommunicationPoint, communicationStepSize)
      :abstractmethod:

      Make a simulation step.

      :param float currentCommunicationPoint: current communication point of the master algorithm (float)
      :param float communicationStepSize: communication step size (float)

   .. py:method:: defineRealParameters(*parameterNames)
      :abstractmethod:

      Define parameters (of type real).

      :param str \*parameterNames: names of parameters of type real

   .. py:method:: defineIntegerParameters(*parameterNames)
      :abstractmethod:

      Define parameters (of type integer).

      :param str \*parameterNames: names of parameters of type integer

   .. py:method:: defineBooleanParameters(*parameterNames)
      :abstractmethod:

      Define parameters (of type boolean).

      :param str \*parameterNames: names of parameters of type boolean

   .. py:method:: defineStringParameters(*parameterNames)
      :abstractmethod:

      Define parameters (of type string).

      :param str \*parameterNames: names of parameters of type string

   .. py:method:: defineRealInputs(*inputVariableNames)
      :abstractmethod:

      Define input variables (of type real).

      :param str \*inputVariableNames: names of input variables of type real

   .. py:method:: defineIntegerInputs(*inputVariableNames)
      :abstractmethod:

      Define input variables (of type integer).

      :param str \*inputVariableNames: names of input variables of type integer

   .. py:method:: defineBooleanInputs(*inputVariableNames)
      :abstractmethod:

      Define input variables (of type boolean).

      :param str \*inputVariableNames: names of input variables of type boolean

   .. py:method:: defineStringInputs(*inputVariableNames)
      :abstractmethod:

      Define input variables (of type string).

      :param str \*inputVariableNames: names of input variables of type string

   .. py:method:: defineRealOutputs(*outputVariableNames)
      :abstractmethod:

      Define output variables (of type real).

      :param str \*outputVariableNames: names of output variables of type real

   .. py:method:: defineIntegerOutputs(*outputVariableNames)
      :abstractmethod:

      Define output variables (of type integer).

      :param str \*outputVariableNames: names of output variables of type integer

   .. py:method:: defineBooleanOutputs(*outputVariableNames)
      :abstractmethod:

      Define output variables (of type boolean).

      :param str \*outputVariableNames: names of output variables of type boolean

   .. py:method:: defineStringOutputs(*outputVariableNames)
      :abstractmethod:

      Define output variables (of type string).

      :param str \*outputVariableNames: names of output variables of type string

   .. py:method:: getRealParameterValues()
      :abstractmethod:

      Retrieve parameters (of type real).

      :return: dict of parameters of type real (includes all parameters of type real previously defined during the initialization)
      :rtype: dict[str, float]

   .. py:method:: getIntegerParameterValues()
      :abstractmethod:

      Retrieve parameters (of type integer).

      :return: dict of parameters of type integer (includes all parameters of type integer previously defined during the initialization)
      :rtype: dict[str, int]

   .. py:method:: getBooleanParameterValues()
      :abstractmethod:

      Retrieve parameters (of type boolean).

      :return: dict of parameters of type boolean (includes all parameters of type boolean previously defined during the initialization)
      :rtype: dict[str, bool]

   .. py:method:: getStringParameterValues()
      :abstractmethod:

      Retrieve parameters (of type string).

      :return: dict of parameters of type string (includes all parameters of type string previously defined during the initialization)
      :rtype: dict[str, str]

   .. py:method:: getRealInputValues()
      :abstractmethod:

      Retrieve input variables (of type real).

      :return: dict of input variables of type real (includes all input variables of type real previously defined during the initialization)
      :rtype: dict[str, float]

   .. py:method:: getIntegerInputValues()
      :abstractmethod:

      Retrieve input variables (of type integer).

      :return: dict of input variables of type real (includes all input variables of type real previously defined during the initialization)
      :rtype: dict[str, int]

   .. py:method:: getBooleanInputValues()
      :abstractmethod:

      Retrieve input variables (of type boolean).

      :return: dict of input variables of type boolean (includes all input variables of type boolean previously defined during the initialization)
      :rtype: dict[str, bool]

   .. py:method:: getStringInputValues()
      :abstractmethod:

      Retrieve input variables (of type string).

      :return: dict of input variables of type string (includes all input variables of type string previously defined during the initialization)
      :rtype: dict[str, str]

   .. py:method:: setRealOutputValues(outputValues)
      :abstractmethod:

      Set output variables (of type real).

      :param outputValues: dict of output variables of type real (must include all output variables of type real previously defined during the initialization)
      :type outputValues: dict[str, float]

   .. py:method:: setIntegerOutputValues(outputValues)
      :abstractmethod:

      Set output variables (of type integer).

      :param outputValues: dict of output variables of type integer (must include all output variables of type integer previously defined during the initialization)
      :type outputValues: dict[str, int]

   .. py:method:: setBooleanOutputValues(outputValues)
      :abstractmethod:

      Set output variables (of type boolean).

      :param outputValues: dict of output variables of type boolean (must include all output variables of type boolean previously defined during the initialization)
      :type outputValues: dict[str, bool]

   .. py:method:: setStringOutputValues(outputValues)
      :abstractmethod:

      Set output variables (of type string).

      :param outputValues: dict of output variables of type string (must include all output variables of type string previously defined during the initialization)
      :type outputValues: dict[str, str]
