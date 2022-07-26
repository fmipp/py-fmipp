Class fmipp.RollbackFMU
=======================

.. py:class:: RollbackFMU([fmuDirUri,] modelIdentifier [, loggingOn=False, timeDiffResolution=1e-4, integratorType=integratorBDF])

   This class implements an easy way to reset the state of an FMU for Model Exchange to a state corresponding to a previous time step using the methods ``saveCurrentStateForRollback()`` and ``releaseRollbackState()``.

   Assume that at time ``t0`` the method call ``integrate( t1 )`` was issued, i.e., the integration of the associated FMU from time ``t0`` to time ``t1`` > ``t0``.
   In case there happend no event during the integration, after the method call the internal state of the FMU corresponds to time ``t1``.
   Now, in order to rollback the FMU to a state corresponding to time ``t2``, with ``t0`` < ``t2`` < ``t1``, the method call ``integrate( t2 )`` is sufficient.

   Internally, class ``RollbackFMU`` stores a rollback state.
   No rollbacks corresponding to a time previous to that internally stored rollback state are possible.
   If not otherwise instructed, the latest stored rollback state is overwritten with the current state, in case the requested integration endpoint is in the future.
   However, the method ``saveCurrentStateForRollback()`` enforces the current state to be stored as rollback state until it is explicitly released with method ``releaseRollbackState()``.
   This allows to make a rollback over more than one time-consecutive integration cycle.

   .. note::

      This class uses objects of type ``SwigPyObject`` as inputs and outputs, which are wrappers around C/C++ arrays.
      Instantiation of and data access to these objects should be done via the :doc:`corresponding helper functions </reference/SwigPyObjects>`.

   :param str fmuDirUri: URI to the :doc:`unzipped FMU </getting-started/loading>`
   :param str modelIdentifier: model identifier of the FMU
   :param bool loggingOn: enable logger for debugging
   :param float timeDiffResolution: internal resolution for comparing time differences
   :param int integratorType: the numerical integration method for solving ODEs (see list of available integrators :doc:`here <FMUModelExchangeV2>`)


   .. rubric:: Methods for interacting with the FMU
      :name: methods_interact_rollback

   .. py:method:: instantiate(instanceName)

      This functions creates a new internal FMU instance.
      This function must be called successfully, before any of the following functions can be called.

      :param str instanceName: a unique identifier for a given FMI component instance, used to identify a component within a co-simulation graph model and for logging messages
      :rtype: int (``statusOK``, ``statusWarning``, ``statusDiscard``, ``statusError`` or ``statusFatal``)

   .. py:method:: initialize(toleranceDefined=False, tolerance=1e-05)

      Informs the FMU instance that the simulation run starts now.

      :param bool toleranceDefined: if ``True``, the model is called with a numerical integration scheme where the step size is controlled by using ``tolerance``
      :param float tolerance: relative tolerance for error estimation
      :rtype: int (``statusOK``, ``statusWarning``, ``statusDiscard``, ``statusError`` or ``statusFatal``)

   .. py:method:: integrate(tstop [, deltaT=1E-5])

      In case there happend no event during the integration, after the method call the internal state of the FMU corresponds to time ``tstop``.
      To rollback the FMU to a state corresponding to time ``trollback``, the method call ``integrate( trollback )`` is sufficient.

      :param float tend: stop time for the integration
      :param int deltaT: starting step size to be used by the integrator, smaller values lead to more accuracy
      :return: integration stop time
      :rtype: float

   .. py:method:: saveCurrentStateForRollback()

      Saves the current state of the FMU as internal rollback state.
      This rollback state will not be overwritten until ``releaseRollbackState()`` is called.

   .. py:method:: releaseRollbackState()

      Realease an internal rollback state, that was previously saved via ``saveCurrentStateForRollback()``.


   .. rubric:: Methods for getting/setting values
      :name: methods_get_set_rollback

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


   .. rubric:: Miscellaneous methods
      :name: methods_misc_rollback

   .. py:method:: getTime()

      :rtype: float

   .. py:method:: getLastStatus()

      :rtype: int (``statusOK``, ``statusWarning``, ``statusDiscard``, ``statusError`` or ``statusFatal``)
