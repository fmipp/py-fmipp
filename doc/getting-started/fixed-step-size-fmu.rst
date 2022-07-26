Classes FixedStepSizeFMU and InterpolatingFixedStepSizeFMU
==========================================================

Classes ``FixedStepSizeFMU`` and ``InterpolatingFixedStepSizeFMU`` ease the use of FMUs for Co-Simulation (currently only FMI Version 1.0) that enforce a fixed time
step, i.e., FMU communication intervals with a fixed length.
The handling is very similar to class ``IncrementalFMU``, i.e., it defines the methods ``defineRealInputs``, ``defineRealOutputs``,
``getRealOutputs``, etc. in an analogous way.
However, ``sync`` always returns the time of the next FMU communication point. 

Whenever calling ``sync`` for a ``FixedStepSizeFMU``, the internal state according to the FMU's latest communication point will be used for retrieving outputs, i.e., it implements a zero-order hold. 
In contrast, class ``InterpolatingFixedStepSizeFMU`` linearly interpolates the outputs according to the FMU's internal state at the previous and the forthcoming communication point.

Whenever an FMU communication point is reached, the latest inputs are handed to the FMU.
This means, that multiple calls of sync between two FMU communication points with different inputs will only cause the latest input to be handed to the FMU (no queueing).

The following example demonstrates the basic usage of class ``FixedStepSizeFMU``:

.. code:: Python

  logging_on = False
  fmu = fmipp.FixedStepSizeFMU( uri_to_extracted_fmu, model_name, logging_on )

  # number of parameter to be initialzed
  n_init = 1

  # construct string array for init parameter names
  init_vars = fmipp.new_string_array( n_init )
  fmipp.string_array_setitem( init_vars, 0, 'omega' )

  # construct double array for init parameter values
  init_vals = fmipp.new_double_array( n_init )
  fmipp.double_array_setitem( init_vals, 0, 0.1 * math.pi )

  # number of outputs
  n_outputs = 1

  # construct string array with output names
  outputs = fmipp.new_string_array( n_outputs )
  fmipp.string_array_setitem( outputs, 0, 'x' )

  # define real output names
  fmu.defineRealOutputs( outputs, n_outputs );

  start_time = 0.
  stop_time = 5.
  fmu_step_size = 1. # fixed step size enforced by FMU
  sim_step_size = 0.2 # step size of simulation
  time = start_time

  status = fmu.init( "test_sine", init_vars, init_vals, n_init, start_time, fmu_step_size )
  assert status == 1

  while ( time <= stop_time ):
    fmu.sync( time, time + sim_step_size )
    time += sim_step_size
    result = fmu.getRealOutputs()

