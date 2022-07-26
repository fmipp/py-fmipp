Class fmipp.IncrementalFMU
==========================

.. py:class:: IncrementalFMU([fmuDirUri,] modelIdentifier [, loggingOn=False, timeDiffResolution=1e-4, integratorType=integratorBDF])

   This class offers the possibility to combine the basic ability to integrate the state of an FMU for ME with advanced event handling capabilities.
   It implements a lookahead mechanism, where predictions of the FMU’s state are incrementally computed and stored.
   In case an event occurs, these predictions are used to interpolate and update the state of the FMU.
   If no event occurs, the latest prediction can be directly used to update the FMU’s state.
   More details can be found `here <https://fmipp.readthedocs.io/en/latest/import.html#class-incrementalfmu>`__.
   An example for using class ``IncrementalFMU`` can be found :doc:`here </getting-started/incremental-fmu>`

   When creating the first instance of this class, the FMU has to be loaded.
   For this, the URI to the :doc:`unzipped FMU </getting-started/loading>` has to be provided:

   .. code-block:: py

      inc_fmu = fmipp.IncrementalFMU(fmuDirUri, modelIdentifier, False, 1e-4, integratorBDF)

   In case you want to have more than one instance of the same FMU, just create another instance of this class without providing the URI to the unzipped FMU (the FMU will have already been loaded in the background the first time):

   .. code-block:: py

      inc_fmu = fmipp.IncrementalFMU(modelIdentifier, False, 1e-4, integratorBDF)

   .. note::

      This class uses objects of type ``SwigPyObject`` as inputs and outputs, which are wrappers around C/C++ arrays.
      Instantiation of and data access to these objects should be done via the :doc:`corresponding helper functions </reference/SwigPyObjects>`.

   :param str fmuDirUri: URI to the :doc:`unzipped FMU </getting-started/loading>`
   :param str modelIdentifier: model identifier of the FMU
   :param bool loggingOn: enable logger for debugging
   :param float timeDiffResolution: internal resolution for comparing time differences
   :param int integratorType: the numerical integration method for solving ODEs (see list of available integrators :doc:`here <FMUModelExchangeV2>`)


   .. rubric:: Methods for interacting with the FMU
      :name: methods_interact_incremental_fmu

   .. py:method:: init(instanceName, realVariableNames, realValues, nRealVars [, integerVariableNames, integerValues, nIntegerVars, booleanVariableNames, booleanValues, nBooleanVars, stringVariableNames, stringValues, nStringVars,] startTime, lookAheadHorizon, lookAheadStepSize, integratorStepSize, toleranceDefined=False, tolerance=1e-5)

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
      :param float startTime: starting time for the internal FMU model
      :param float lookAheadHorizon: lookahead horizon, i.e., time interval for calculating predictions
      :param float lookAheadStepSize: time interval between predictions
      :param float integratorStepSize: starting step size to be used by the integrator, smaller values lead to more accuracy
      :param bool toleranceDefined: if ``True``, the model is called with a numerical integration scheme where the step size is controlled by using ``tolerance``
      :param float tolerance: relative tolerance for error estimation
      :rtype: int
      :return: 1 on success, 0 on failure

   .. py:method:: updateState(t1)

      Updates the state of the FMU to the specified time ``t1``, i.e., it changes the actual state using the previous state prediction(s).
      The specified time must not be further ahead than the lookahead horizon.
      The function has to be called after ``predictState(...)`` was called.

      :param float t1: synchronization time
      :rtype: float
      :return: the internal FMU model's current simulation time


   .. py:method:: updateStateFromTheRight(t1)

      Updates the FMU's state to the predicted state at time ``t1``.
      The specified time must not be further ahead than the lookahead horizon.
      In case of a discontinuity at t1, the FMU's outputs will reflect the limit from the right.
      The function may enhance time by the ``timeDiffResulution`` set at construction time.
      The function has to be called after ``predictState(...)`` was called and may be used instead of updateState() which always sets the limit from the left.

      :param float t1: synchronization time
      :rtype: float
      :return: the internal FMU model's current simulation time

   .. py:method:: syncState(t1, realInputs, integerInputs, booleanInputs, stringInputs)

      Sets the given inputs at the FMU at time ``t1`` and fetches the updated current state.
      The function assumes that ``updateState()`` or ``updateStateFromTheRight()`` was called before.

      :param float t1: synchronization time
      :param SwigPyObject realInputs: real inputs, previously defined via ``defineRealInputs(...)``
      :param SwigPyObject integerInputs: integer inputs, previously defined via ``defineIntegerInputs(...)``
      :param SwigPyObject booleanInputs: boolean inputs, previously defined via ``defineBooleanInputs(...)``
      :param SwigPyObject stringInputs: string inputs, previously defined via ``defineStringInputs(...)``

   .. py:method:: predictState(t1)

      Compute the state predictions according to the latest inputs.

      :rtype: float
      :return: the time of the last state prediction, corresponding either to the lookahead horizon or the next encountered event time

   .. py:method:: sync(t0, t1 [, realInputs, integerInputs, booleanInputs, stringInputs])

      This method executes ``updateState(...)``, ``syncState(...)`` and ``predictState(...)`` in one go.

      :param float t0: simulation interval start time
      :param float t1: simulation interval end time
      :param SwigPyObject realInputs: real inputs, previously defined via ``defineRealInputs(...)``
      :param SwigPyObject integerInputs: integer inputs, previously defined via ``defineIntegerInputs(...)``
      :param SwigPyObject booleanInputs: boolean inputs, previously defined via ``defineBooleanInputs(...)``
      :param SwigPyObject stringInputs: string inputs, previously defined via ``defineStringInputs(...)``
      :rtype: float
      :return: the time of the last state prediction, corresponding either to the lookahead horizon or the next encountered event time


   .. rubric:: Methods for defining inputs/outputs
      :name: methods_define_incremental_fmu

   .. py:method:: defineBooleanInputs(inputs, nInputs)

      Define boolean inputs to be applied to the FMU via the ``sync(...)`` method.

      :param SwigPyObject inputs: initial values of the input variables
      :param int nInputs: number of boolean inputs

   .. py:method:: defineBooleanOutputs(outputs, nOutputs)

      Define boolean outputs to be retrieved from the FMU via the ``getBooleanOutputs(...)`` method.

      :param SwigPyObject outputs: initial values of the output variables
      :param int nOutputs: number of boolean outputs

   .. py:method:: defineIntegerInputs(inputs, nInputs)

      Define integer inputs to be applied to the FMU via the ``sync(...)`` method.

      :param SwigPyObject inputs: initial values of the input variables
      :param int nInputs: number of integer inputs

   .. py:method:: defineIntegerOutputs(outputs, nOutputs)

      Define integer outputs to be retrieved from the FMU via the ``getIntegerOutputs(...)`` method.

      :param SwigPyObject outputs: initial values of the output variables
      :param int nOutputs: number of integer outputs

   .. py:method:: defineRealInputs(inputs, nInputs)

      Define real inputs to be applied to the FMU via the ``sync(...)`` method.

      :param SwigPyObject inputs: initial values of the input variables
      :param int nInputs: number of real inputs

   .. py:method:: defineRealOutputs(outputs, nOutputs)

      Define real outputs to be retrieved from the FMU via the ``getRealOutputs(...)`` method.

      :param SwigPyObject outputs: initial values of the output variables
      :param int nOutputs: number of real outputs

   .. py:method:: defineStringInputs(inputs, nInputs)

      Define string inputs to be applied to the FMU via the ``sync(...)`` method.

      :param SwigPyObject inputs: initial values of the input variables
      :param int nInputs: number of string inputs

   .. py:method:: defineStringOutputs(outputs, nOutputs)

      Define string outputs to be retrieved from the FMU via the ``getStringOutputs(...)`` method.

      :param SwigPyObject outputs: initial values of the output variables
      :param int nOutputs: number of string outputs


   .. rubric:: Methods for getting variable values
      :name: methods_get_incremental_fmu

   .. py:method:: getBooleanOutputs()

      :rtype: SwigPyObject
      :return: value of boolean outputs

   .. py:method:: getIntegerOutputs()

      :rtype: SwigPyObject
      :return: value of integer outputs

   .. py:method:: getRealOutputs()

      :rtype: SwigPyObject
      :return: value of real outputs

   .. py:method:: getStringOutputs()

      :rtype: SwigPyObject
      :return: value of string outputs


   .. rubric:: Miscellaneous methods
      :name: methods_misc_incremental_fmu

   .. py:method:: getTimeDiffResolution()

      :return: internal resolution for comparing time differences
      :rtype: float

   .. py:method:: getType(name)

   	Get information about the type of a variable.

      :param str name: variable name
      :rtype: int (``typeReal``, ``typeInteger``, ``typeBoolean``, ``typeString`` or ``typeUnknown``)

   .. py:method:: getLastStatus()

      :return: status returned by latest internal FMU function call
      :rtype: int (``statusOK``, ``statusWarning``, ``statusDiscard``, ``statusError`` or ``statusFatal``)
