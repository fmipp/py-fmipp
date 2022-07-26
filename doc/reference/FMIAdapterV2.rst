Class fmipp.export.FMIAdapterV2
===============================

.. py:class:: FMIAdapterV2()

   Abtract base class for defining FMUs for Co-Simulation compliant to FMI version 2.0.
   To implement an FMU, inherit a new class from class :doc:`FMIAdapterBase </reference/FMIAdapterBase>` that implements the methods ``init(…)`` and ``doStep(…)``
   This class is a user-friendly wrapper for the functionality provided by the SWIG-generated Python bindings of the FMI++ library.
   See `here <https://github.com/fmipp/py-fmipp-tutorial/blob/master/demos/TestFMUExport.ipynb>`__ and `here <https://github.com/fmipp/py-fmipp-tutorial/blob/master/demos/TestFMUExportDebug.ipynb>`__ for an example of usage.

   .. rubric:: Ancestors
      :name: ancestors

   -  :doc:`fmipp.export.FMIAdapterBase.FMIAdapterBase </reference/FMIAdapterBase>`

   .. rubric:: Abstract Methods
      :name: FMIAdapterV2-abstract-methods
   
   .. py:method:: init(currentCommunicationPoint)
      :abstractmethod:

      Initialize the FMU (definition of input/output variables and parameters, enforce step size).
      
      :param float currentCommunicationPoint: current communication point of the master algorithm during initialization (float)
   
   .. py:method:: doStep(currentCommunicationPoint, communicationStepSize)
      :abstractmethod:
   
      Make a simulation step.
      
      :param float currentCommunicationPoint: current communication point of the master algorithm (float) 
      :param float communicationStepSize: communication step size (float)
   
   .. rubric:: Methods
      :name: FMIAdapterV2-methods

   .. py:method:: defineRealParameters(*parameterNames)
   
      Define parameters (of type real).
      
      :param str \*parameterNames: names of parameters of type real
   
   .. py:method:: defineIntegerParameters(*parameterNames)
   
      Define parameters (of type integer).
      
      :param str \*parameterNames: names of parameters of type integer
   
   .. py:method:: defineBooleanParameters(*parameterNames)
   
      Define parameters (of type boolean).
      
      :param str \*parameterNames: names of parameters of type boolean
   
   .. py:method:: defineStringParameters(*parameterNames)
   
      Define parameters (of type string).
      
      :param str \*parameterNames: names of parameters of type string
   
   .. py:method:: defineRealInputs(*inputVariableNames)
   
      Define input variables (of type real).
      
      :param str \*inputVariableNames: names of input variables of type real
   
   .. py:method:: defineIntegerInputs(*inputVariableNames)
   
      Define input variables (of type integer).
      
      :param str \*inputVariableNames: names of input variables of type integer
   
   .. py:method:: defineBooleanInputs(*inputVariableNames)
   
      Define input variables (of type boolean).
      
      :param str \*inputVariableNames: names of input variables of type boolean
   
   .. py:method:: defineStringInputs(*inputVariableNames)
   
      Define input variables (of type string).
      
      :param str \*inputVariableNames: names of input variables of type string
   
   .. py:method:: defineRealOutputs(*outputVariableNames)
   
      Define output variables (of type real).
      
      :param str \*outputVariableNames: names of output variables of type real
   
   .. py:method:: defineIntegerOutputs(*outputVariableNames)
   
      Define output variables (of type integer).
      
      :param str \*outputVariableNames: names of output variables of type integer
   
   .. py:method:: defineBooleanOutputs(*outputVariableNames)
   
      Define output variables (of type boolean).
      
      :param str \*outputVariableNames: names of output variables of type boolean
   
   .. py:method:: defineStringOutputs(*outputVariableNames)
   
      Define output variables (of type string).
      
      :param str \*outputVariableNames: names of output variables of type string
   
   .. py:method:: getRealParameterValues()
   
      Retrieve parameters (of type real).
      
      :return: dict of parameters of type real (includes all parameters of type real previously defined during the initialization)
      :rtype: dict[str, float]
   
   .. py:method:: getIntegerParameterValues()
   
      Retrieve parameters (of type integer).
      
      :return: dict of parameters of type integer (includes all parameters of type integer previously defined during the initialization)
      :rtype: dict[str, int]
   
   .. py:method:: getBooleanParameterValues()
   
      Retrieve parameters (of type boolean).
      
      :return: dict of parameters of type boolean (includes all parameters of type boolean previously defined during the initialization)
      :rtype: dict[str, bool]
   
   .. py:method:: getStringParameterValues()
   
      Retrieve parameters (of type string).
      
      :return: dict of parameters of type string (includes all parameters of type string previously defined during the initialization)
      :rtype: dict[str, str]
   
   .. py:method:: getRealInputValues()
   
      Retrieve input variables (of type real).
      
      :return: dict of input variables of type real (includes all input variables of type real previously defined during the initialization)
      :rtype: dict[str, float]
   
   .. py:method:: getIntegerInputValues()
   
      Retrieve input variables (of type integer).
      
      :return: dict of input variables of type real (includes all input variables of type real previously defined during the initialization)
      :rtype: dict[str, int]
   
   .. py:method:: getBooleanInputValues()
   
      Retrieve input variables (of type boolean).
      
      :return: dict of input variables of type boolean (includes all input variables of type boolean previously defined during the initialization)
      :rtype: dict[str, bool]
   
   .. py:method:: getStringInputValues()
   
      Retrieve input variables (of type string).
      
      :return: dict of input variables of type string (includes all input variables of type string previously defined during the initialization)
      :rtype: dict[str, str]
   
   .. py:method:: setRealOutputValues(outputValues)
   
      Set output variables (of type real).
      
      :param outputValues: dict of output variables of type real (must include all output variables of type real previously defined during the initialization)
      :type outputValues: dict[str, float]
   
   .. py:method:: setIntegerOutputValues(outputValues)
   
      Set output variables (of type integer).
      
      :param outputValues: dict of output variables of type integer (must include all output variables of type integer previously defined during the initialization)
      :type outputValues: dict[str, int]
   
   .. py:method:: setBooleanOutputValues(outputValues)
   
      Set output variables (of type boolean).
      
      :param outputValues: dict of output variables of type boolean (must include all output variables of type boolean previously defined during the initialization)
      :type outputValues: dict[str, bool]
   
   .. py:method:: setStringOutputValues(outputValues)
   
      Set output variables (of type string).
      
      :param outputValues: dict of output variables of type string (must include all output variables of type string previously defined during the initialization)
      :type outputValues: dict[str, str]
   
