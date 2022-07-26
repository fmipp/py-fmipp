Class RollbackFMU
=================

Class :doc:`RollbackFMU </reference/RollbackFMU>` implements an easy way to reset the state of a given FMU for ModelExchange (FMI Version 1.0 and 2.0) to a state according to a previous time step.

Assume that at time ``t0`` the function call ``integrate( t1 )`` was issued, i.e., the integration of the associated FMU from time ``t0`` to time ``t1 > t0``.
In case there happend no event during the integration, after the function call the internal state of the FMU corresponds to time ``t1``.
Now, in order to rollback the FMU to a state corresponding to time ``t2``, with ``t0 < t2 < t1``, the function call ``integrate( t2 )`` is sufficient.
Internally, class ``RollbackFMU`` stores a rollback state.
No rollbacks corresponding to a time previous to that internally stored rollback state are possible.
If not otherwise instructed, the latest stored rollback state is overwritten with the current state, in case the integration endpoint is in the
future.
However, the method ``saveCurrentStateForRollback`` enforces the current state to be stored as rollback state until it is explicitly released with method ``releaseRollbackState``.
This allows to make a rollback over more than one time-consecutive integration cycle.

The following example demonstrates the basic usage of class ``RollbackFMU``:

.. code:: Python

  logging_on = False
  fmu = fmipp.RollbackFMU( uri_to_extracted_fmu, model_name )

  instance_name = 'zigzag1'
  status = fmu.instantiate( instance_name )
  assert status == fmipp.statusOK

  status = fmu.setRealValue( 'k', 1.0 )
  assert status == fmipp.statusOK

  status = fmu.initialize()
  assert status == fmipp.statusOK

  time = 0.0 
  step_size = 0.025
  stop_time = 0.5
  x = -1.0

  while ( ( time + step_size ) - stop_time < 1e-6 ):
    # Make integration step.
    fmu.integrate( time + step_size )

    # Enforce rollback.
    fmu.integrate( time + 0.5*step_size )
    time = fmu.integrate( time + step_size )
    x = fmu.getRealValue( 'x' )
