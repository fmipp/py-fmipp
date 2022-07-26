Class fmipp.FMUCoSimulationV2
=============================

.. py:class:: FMUCoSimulationV2([fmuDirUri,] modelIdentifier [, loggingOn=False, timeDiffResolution=1e-9])

   This class provides a basic Python wrapper that offers a set of convenient methods for accessing and manipulating FMUs for Co-Simulation according to the **FMI CS V2.0 standard**.
   Instances of class ``FMUCoSimulationV2`` own the actual FMU instance.

   When creating the first instance of this class, the FMU has to be loaded.
   For this, the URI to the :doc:`unzipped FMU </getting-started/loading>` has to be provided:

   .. code-block:: py

      fmu = fmipp.FMUCoSimulationV2(fmuDirUri, modelIdentifier, False, 1e-9)

   An FMU can be instantiated many times (provided capability flag ``canBeInstantiatedOnlyOncePerProcess`` is ``False``).
   In case you want to have more than one instance of the same FMU, just create another instance of this class without providing the URI to the unzipped FMU (the FMU will have already been loaded in the background the first time):

   .. code-block:: py

      fmu = fmipp.FMUCoSimulationV2(modelIdentifier, False, 1e-9)

   :param str fmuDirUri: URI to the :doc:`unzipped FMU </getting-started/loading>`
   :param str modelIdentifier: model identifier of the FMU
   :param bool loggingOn: enable logger for debugging
   :param float timeDiffResolution: internal resolution for comparing time differences


   .. rubric:: Methods for interacting with the FMU
      :name: methods_interact_cs2

   .. py:method:: instantiate(instanceName, timeout, visible, interactive)

      This functions creates a new internal FMU instance.
      This function must be called successfully, before any of the following functions can be called.

      :param str instanceName: a unique identifier for a given FMI component instance, used to identify a component within a co-simulation graph model and for logging messages
      :param float timeout:  a communication timeout value in milli-seconds to allow interprocess communication to take place (a value of 0 indicates an infinite wait period)
      :param bool visible: indicates whether or not the simulator application window needed to execute a model should be visible (``False`` indicates that the simulator is executed in batch mode, ``True`` indicates that the simulator is executed in interactive mode)
      :param bool interactive: indicates whether the simulator application must be manually started by the user (``False`` indicates that the co-simulation tool automatically starts the simulator application and executes the model referenced in the model description, ``True`` indicates that the simulator application must be manually started by the user)
      :rtype: int (``statusOK``, ``statusWarning``, ``statusDiscard``, ``statusError`` or ``statusFatal``)

   .. py:method:: initialize(startTime, stopTimeDefined, stopTime)

      Informs the FMU instance that the simulation run starts now.

      :param float startTime: can be used together with ``stopTime`` to check whether the model is valid within the given boundaries or to allocate memory which is necessary for storing results
      :param bool stopTimeDefined: if ``True``, the FMU returns ``statusError`` if the environment tries to compute past ``stopTime``.
      :param float stopTime: can be used together with ``startTime`` to check whether the model is valid within the given boundaries or to allocate memory which is necessary for storing results
      :rtype: int (``statusOK``, ``statusWarning``, ``statusDiscard``, ``statusError`` or ``statusFatal``)

   .. py:method:: doStep(currentCommunicationPoint, communicationStepSize, newStep)

      The computation of a time step is started.

      :param float currentCommunicationPoint: current communication point of the cco-simulation algorithm
      :param float communicationStepSize: communication step size (if the co-simulation algorithm carries out an event iteration the parameter is 0)
      :param bool newStep: parameter not used (only for consistency with methods ``doStep`` from class ``FMUCoSimulationV1``)
      :rtype: int (``statusOK``, ``statusWarning``, ``statusDiscard``, ``statusError`` or ``statusFatal``)

   .. py:method:: terminate()

      Is called by the co-simulation algorithm to signal the end of the co-simulation run.


   .. rubric:: Methods for getting/setting values
      :name: methods_get_set_cs2

   .. py:method:: getBooleanValue(name)

      :param str name: variable name
      :rtype: bool

   .. py:method:: getIntegerValue(name)

      :param str name: variable name
      :rtype: int

   .. py:method:: getRealValue(name)

      :param str name: variable name
      :rtype: float

   .. py:method:: getStringValue(name)

      :param str name: variable name
      :rtype: str

   .. py:method:: getLastStatus()

      :rtype: int (``statusOK``, ``statusWarning``, ``statusDiscard``, ``statusError`` or ``statusFatal``)

   .. py:method:: getTime()

      :rtype: float

   .. py:method:: getType(name)

   	Get information about the type of a variable.

      :param str name: variable name
      :rtype: int (``typeReal``, ``typeInteger``, ``typeBoolean``, ``typeString`` or ``typeUnknown``)

   .. py:method:: getValueRef(name)

      Get the value reference of a variable.

      :param str name: variable name
      :rtype: int

   .. py:method:: setBooleanValue(name, val)

      :param str name: variable name
      :param bool val: vew value for the variable
      :rtype: int (``statusOK``, ``statusWarning``, ``statusDiscard``, ``statusError`` or ``statusFatal``)

   .. py:method:: setIntegerValue(name, val)

      :param str name: variable name
      :param int val: vew value for the variable
      :rtype: int (``statusOK``, ``statusWarning``, ``statusDiscard``, ``statusError`` or ``statusFatal``)

   .. py:method:: setRealValue(name, val)

      :param str name: variable name
      :param float val: vew value for the variable
      :rtype: int (``statusOK``, ``statusWarning``, ``statusDiscard``, ``statusError`` or ``statusFatal``)

   .. py:method:: setStringValue(name, val)

      :param str name: variable name
      :param str val: vew value for the variable
      :rtype: int (``statusOK``, ``statusWarning``, ``statusDiscard``, ``statusError`` or ``statusFatal``)


   .. rubric:: Methods for retrieving model description flags
      :name: methods_flags_cs2

   .. py:method:: canBeInstantiatedOnlyOncePerProcess()

      :rtype: bool

   .. py:method:: canHandleEvents()

      :rtype: bool

   .. py:method:: canHandleVariableCommunicationStepSize()

      :rtype: bool

   .. py:method:: canInterpolateInputs()

      :rtype: bool

   .. py:method:: canNotUseMemoryManagementFunctions()

      :rtype: bool

   .. py:method:: canRejectSteps()

      :rtype: bool

   .. py:method:: canRunAsynchronuously()

      :rtype: bool

   .. py:method:: canSignalEvents()

      :rtype: bool

   .. py:method:: maxOutputDerivativeOrder()

      :rtype: int

   .. py:method:: nEventInds()

      :rtype: int

   .. py:method:: nStates()

      :rtype: int

   .. py:method:: nValueRefs()

      :rtype: int


   .. rubric:: Miscellaneous methods
      :name: methods_misc_cs2

   .. py:method:: setCallbacks(logger, allocateMemory, freeMemory, stepFinished)

      Set FMU callback functions.

      :rtype: int (``statusOK``, ``statusWarning``, ``statusDiscard``, ``statusError`` or ``statusFatal``)

   .. py:method:: setComponentEnvironment(env)

      Set a pointer to a data structure in the simulation environment that calls the FMU.
      Via this pointer, data from the model description file can be transferred between the simulation environment and the logger function.

   .. py:method:: logger(status, category, msg)

      Call the FMU's logger.

      :param int status: logger status
      :param str category: logger category
      :param str msg: logger message

   .. py:method:: sendDebugMessage(msg)

      Send a debug message.

      :param str msg: debug message
