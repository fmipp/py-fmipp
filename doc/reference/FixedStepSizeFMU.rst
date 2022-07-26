Class fmipp.FixedStepSizeFMU
============================

.. py:class:: FixedStepSizeFMU(fmuDirUri, modelIdentifier [, loggingOn=False, timeDiffResolution=1e-4])

   This class eases the use of FMUs for Co-Simulation that enforce a fixed time step, i.e., FMU communication intervals with a fixed length.
   Its handling is very similar to class :doc:`IncrementalFMU </getting-started/incremental-fmu>`, i.e., it defines the methods ``defineRealInputs(...)``, ``defineRealOutputs(...)``, ``getRealOutputs(...)``, etc. in an analogous way.
   However, method ``sync(...)`` always synchronizes the internal state to the FMU state corresponding to the latest FMU communication point, i.e., it implements a zero-order hold.

   .. note::

      This class uses objects of type ``SwigPyObject`` as inputs and outputs, which are wrappers around C/C++ arrays.
      Instantiation of and data access to these objects should be done via the :doc:`corresponding helper functions </reference/SwigPyObjects>`.

   :param str fmuDirUri: URI to the :doc:`unzipped FMU </getting-started/loading>`
   :param str modelIdentifier: model identifier of the FMU
   :param bool loggingOn: enable logger for debugging
   :param float timeDiffResolution: internal resolution for comparing time differences


.. rubric:: Methods for interacting with the FMU
   :name: methods_interact_fixed_step

.. py:function:: init(self, instanceName, realVariableNames, realValues, nRealVars, [integerVariableNames, integerValues, nIntegerVars, booleanVariableNames, booleanValues, nBooleanVars, stringVariableNames, stringValues, nStringVars,] startTime, communicationStepSize [,stopTimeDefined=False, stopTime=float('inf'), timeout=0, visible=False, interactive=False])
   :noindex:

   Initialize the internal FMU model.

   :param str instanceName: a unique identifier for a given FMI component instance, used to identify a component within a co-simulation graph model and for logging messages
   :param SwigPyObject realVariableNames: names of real variables
   :param SwigPyObject realValues: initial values of real variables
   :param int nRealVars: number of real variables to be initialized
   :param SwigPyObject integerVariableNames: names of integer variables
   :param SwigPyObject integerValues: initial values of integer variables
   :param int nIntegerVars: number of integer variables to be initialized
   :param SwigPyObject booleanVariableNames: names of boolean variables
   :param SwigPyObject booleanValues: initial values of boolean variables
   :param int nBooleanVars: number of boolean variables to be initialized
   :param SwigPyObject stringVariableNames: names of string variables
   :param SwigPyObject stringValues: initial values of string variables
   :param int nStringVars: number of string variables to be initialized
   :param float startTime: can be used together with ``stopTime`` to check whether the model is valid within the given boundaries or to allocate memory which is necessary for storing results
   :param float communicationStepSize: fixed communication step size
   :param bool stopTimeDefined: if ``True``, the FMU returns ``statusError`` if the environment tries to compute past ``stopTime``.
   :param float stopTime: can be used together with ``startTime`` to check whether the model is valid within the given boundaries or to allocate memory which is necessary for storing results
   :param float timeout:  a communication timeout value in milli-seconds to allow interprocess communication to take place (a value of 0 indicates an infinite wait period)
   :param bool visible: indicates whether or not the simulator application window needed to execute a model should be visible (``False`` indicates that the simulator is executed in batch mode, ``True`` indicates that the simulator is executed in interactive mode)
   :param bool interactive: indicates whether the simulator application must be manually started by the user (``False`` indicates that the co-simulation tool automatically starts the simulator application and executes the model referenced in the model description, ``True`` indicates that the simulator application must be manually started by the user)
   :rtype: int
   :return: 1 on success, 0 on failure

.. py:function:: sync(self, t0, t1 [, realInputs, integerInputs, booleanInputs, stringInputs, iterateOnce=False])
   :noindex:

   Simulate FMU from time ``t0`` until ``t1``.
   If provided, the inputs are set at the *end* of the interval [``t0``, ``t1``].
   Method ``sync(...)`` always returns the time of the next FMU communication point.
   Whenever an FMU communication point is reached, the latest inputs are handed to the FMU.
   This means, that multiple calls to ``sync(...)`` between two FMU communication points with different inputs will only cause the latest input to be handed to the FMU (no queueing).

   :param float t0: simulation interval start time
   :param float t1: simulation interval end time
   :param SwigPyObject realInputs: real inputs, previously defined via ``defineRealInputs(...)``
   :param SwigPyObject integerInputs: integer inputs, previously defined via ``defineIntegerInputs(...)``
   :param SwigPyObject booleanInputs: boolean inputs, previously defined via ``defineBooleanInputs(...)``
   :param SwigPyObject stringInputs: string inputs, previously defined via ``defineStringInputs(...)``
   :param bool iterateOnce: if ``True``, iterate the FMU (simulation step with length 0) at time ``t1``
   :rtype: float
   :return: time of the next FMU communication point

.. py:function:: iterateOnce(self)
   :noindex:

   Iterate the FMU (simulation step with length 0).


.. rubric:: Methods for defining inputs/outputs
   :name: methods_define_fixed_step

.. py:function:: defineBooleanInputs(self, inputs, nInputs)
   :noindex:

   Define boolean inputs to be applied to the FMU via the ``sync(...)`` method.

   :param SwigPyObject inputs: initial values of the input variables
   :param int nInputs: number of boolean inputs

.. py:function:: defineBooleanOutputs(self, outputs, nOutputs)
   :noindex:

   Define boolean outputs to be retrieved from the FMU via the ``getBooleanOutputs(...)`` method.

   :param SwigPyObject outputs: initial values of the output variables
   :param int nOutputs: number of boolean outputs

.. py:function:: defineIntegerInputs(self, inputs, nInputs)
   :noindex:

   Define integer inputs to be applied to the FMU via the ``sync(...)`` method.

   :param SwigPyObject inputs: initial values of the input variables
   :param int nInputs: number of integer inputs

.. py:function:: defineIntegerOutputs(self, outputs, nOutputs)
   :noindex:

   Define integer outputs to be retrieved from the FMU via the ``getIntegerOutputs(...)`` method.

   :param SwigPyObject outputs: initial values of the output variables
   :param int nOutputs: number of integer outputs

.. py:function:: defineRealInputs(self, inputs, nInputs)
   :noindex:

   Define real inputs to be applied to the FMU via the ``sync(...)`` method.

   :param SwigPyObject inputs: initial values of the input variables
   :param int nInputs: number of real inputs

.. py:function:: defineRealOutputs(self, outputs, nOutputs)
   :noindex:

   Define real outputs to be retrieved from the FMU via the ``getRealOutputs(...)`` method.

   :param SwigPyObject outputs: initial values of the output variables
   :param int nOutputs: number of real outputs

.. py:function:: defineStringInputs(self, inputs, nInputs)
   :noindex:

   Define string inputs to be applied to the FMU via the ``sync(...)`` method.

   :param SwigPyObject inputs: initial values of the input variables
   :param int nInputs: number of string inputs

.. py:function:: defineStringOutputs(self, outputs, nOutputs)
   :noindex:

   Define string outputs to be retrieved from the FMU via the ``getStringOutputs(...)`` method.

   :param SwigPyObject outputs: initial values of the output variables
   :param int nOutputs: number of string outputs


.. rubric:: Methods for getting variable values
   :name: methods_get_fixed_step

.. py:function:: getBooleanOutputs(self)
   :noindex:

   :rtype: SwigPyObject
   :return: value of boolean outputs

.. py:function:: getIntegerOutputs(self)
   :noindex:

   :rtype: SwigPyObject
   :return: value of integer outputs

.. py:function:: getRealOutputs(self)
   :noindex:

   :rtype: SwigPyObject
   :return: value of real outputs

.. py:function:: getStringOutputs(self)
   :noindex:

   :rtype: SwigPyObject
   :return: value of string outputs


.. rubric:: Miscellaneous methods
   :name: methods_misc_fixed_step

.. py:function:: getLastStatus(self)
   :noindex:

   :return: status returned by latest internal FMU function call
   :rtype: int (``statusOK``, ``statusWarning``, ``statusDiscard``, ``statusError`` or ``statusFatal``)
