Class fmipp.FMUModelExchangeV2
==============================

.. py:class:: FMUModelExchangeV2([fmuDirUri,] modelIdentifier [, loggingOn=False, stopBeforeEvent=False, eventSearchPrecision=1e-4, type=integratorBDF])

   This class provides a basic Python wrapper that offers a set of convenient methods for accessing and manipulating FMUs for Model Exchange according to the **FMI ME V1.0 standard**.
   Instances of class ``FMUModelExchangeV2`` own the actual FMU instance.

   When creating the first instance of this class, the FMU has to be loaded.
   For this, the URI to the :doc:`unzipped FMU </getting-started/loading>` has to be provided:

   .. code-block:: py

      fmu = fmipp.FMUModelExchangeV2(fmuDirUri, modelIdentifier, False, 1e-4, integratorBDF)

   An FMU can be instantiated many times (provided capability flag ``canBeInstantiatedOnlyOncePerProcess`` is ``False``).
   In case you want to have more than one instance of the same FMU, just create another instance of this class without providing the URI to the unzipped FMU (the FMU will have already been loaded in the background the first time):

   .. code-block:: py

      fmu = fmipp.FMUModelExchangeV2(modelIdentifier, False, 1e-4, integratorBDF)

   The available numerical integrators are listed in the following table:

   +--------------------+----------------------------------+-------+----------+------------------------------------------------+
   | Stepper            | Name                             | Order | Adaptive | Recommended usecases                           |
   +====================+==================================+=======+==========+================================================+
   | ``integratorEU``   | Explicit Euler                   | 1     | No       | Testing                                        |
   +--------------------+----------------------------------+-------+----------+------------------------------------------------+
   | ``integratorRK``   | 4th order Runge-Kutta            | 4     | No       | Testing                                        |
   +--------------------+----------------------------------+-------+----------+------------------------------------------------+
   | ``integratorABM``  | Adams-Bashforth-Moulton          | 8     | No       | Testing                                        |
   +--------------------+----------------------------------+-------+----------+------------------------------------------------+
   | ``integratorCK``   | Cash-Karp                        | 5     | Yes      | Nonstiff Models                                |
   +--------------------+----------------------------------+-------+----------+------------------------------------------------+
   | ``integratorDP``   | Dormand-Prince                   | 5     | Yes      | Nonstiff Models                                |
   +--------------------+----------------------------------+-------+----------+------------------------------------------------+
   | ``integratorFE``   | Fehlberg                         | 8     | Yes      | Nonstiff, smooth Models                        |
   +--------------------+----------------------------------+-------+----------+------------------------------------------------+
   | ``integratorBS``   | Bulirsch Stoer                   | 1-16  | Yes      | High precision required                        |
   +--------------------+----------------------------------+-------+----------+------------------------------------------------+
   | ``integratorRO``   | Rosenbrock                       | 4     | Yes      | Stiff Models                                   |
   +--------------------+----------------------------------+-------+----------+------------------------------------------------+
   | ``integratorBDF``  | Backward Differentiation Formula | 1-5   | Yes      | Stiff Models                                   |
   +--------------------+----------------------------------+-------+----------+------------------------------------------------+
   | ``integratorABM2`` | Adams-Bashforth-Moulton          | 1-12  | Yes      | Nonstiff Models with expensive right hand side |
   +--------------------+----------------------------------+-------+----------+------------------------------------------------+

   :param str fmuDirUri: URI to the :doc:`unzipped FMU </getting-started/loading>`
   :param str modelIdentifier: model identifier of the FMU
   :param bool loggingOn: enable logger for debugging
   :param bool stopBeforeEvent: if ``True``, integration stops immediately before an event
   :param bool eventSearchPrecision: numerical search precision for events during integration
   :param int type: the numerical integration method for solving ODEs (see table above)


   .. rubric:: Methods for interacting with the FMU
      :name: methods_interact_me2

   .. py:method:: instantiate(instanceName)

      This functions creates a new internal FMU instance.
      This function must be called successfully, before any of the following functions can be called.

      :param str instanceName: a unique identifier for a given FMI component instance, used to identify a component within a co-simulation graph model and for logging messages
      :rtype: int (``statusOK``, ``statusWarning``, ``statusDiscard``, ``statusError`` or ``statusFatal``)

   .. py:method:: initialize([toleranceDefined=False, tolerance=1e-05])

      Informs the FMU instance that the simulation run starts now.

      :param bool toleranceDefined: if ``True``, the model is called with a numerical integration scheme where the step size is controlled by using ``tolerance``
      :param float tolerance: relative tolerance for error estimation
      :rtype: int (``statusOK``, ``statusWarning``, ``statusDiscard``, ``statusError`` or ``statusFatal``)

   .. py:method:: integrate(tend[, deltaT=1e-05])

      Integrates the FMU model until time ``tend`` or until the first event.
      The exact behaviour depends on the flag ``stopBeforeEvent``.

      :param float tend: stop time for the integration
      :param int deltaT: starting step size to be used by the integrator, smaller values lead to more accuracy
      :return: integration stop time
      :rtype: float

   .. py:method:: integrateN(tend, nsteps)

      Integrates the FMU model until time ``tend`` or until the first event.
      The exact behaviour depends on the flag ``stopBeforeEvent``.

      :param float tend: stop time for the integration
      :param int nsteps: number of integrator steps to be *recommended* to the integrator, bigger values lead to more accuracy
      :return: integration stop time
      :rtype: float


   .. rubric:: Methods for getting/setting values
      :name: methods_get_set_me2

   .. seealso:: Use the helper functions from module ``fmipp.numeric`` for retrieving derivatives and jacobians from the FMU model.

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


   .. rubric:: Methods for event handling
      :name: methods_event_handling_me2

   .. py:method:: checkEvents()

      Check if any kind of event has happened.

      :rtype: bool

   .. py:method:: checkStateEvent()

      Check if a state event has happened.

      :rtype: bool

   .. py:method:: checkStepEvent()

      Check if a step event has happened.

      :rtype: bool

   .. py:method:: checkTimeEvent()

      Check if a time event has happened.

      :rtype: bool

   .. py:method:: getEventSearchPrecision()

      Get the event search precision.

      :rtype: float

   .. py:method:: getTimeEvent()

      Get the time of the next time event (infinity if no time event is returned by the FMU model).

      :rtype: float

   .. py:method:: handleEvents()

      Handle events.
      Just call this function if actually an event has happened.

   .. py:method:: raiseEvent()

      Raise an event, i.e., notify that an (external) event has occured.

   .. py:method:: resetEventFlags()

      Reset all internal flags related to event handling.

   .. py:method:: stepOverEvent()

      If ``stopBeforeEvent`` is ``True``, use this function to get the right-sided limit of an event.


   .. rubric:: Methods for retrieving model description flags
      :name: methods_flags_me2

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
      :name: methods_misc_me2

   .. py:method:: setCallbacks(logger, allocateMemory, freeMemory)

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
