Classes FMUCoSimulationV1 and FMUCoSimulationV2
=================================================

Classes :doc:`FMUCoSimulationV1 </reference/FMUCoSimulationV1>` (FMI 1.0) and :doc:`FMUCoSimulationV2 </reference/FMUCoSimulationV2>` (FMI 2.0) offer a set of convenient functionalities for accessing and manipulating FMUs for Co-Simulation.
The following example demonstrates the basic usage of class ``FMUCoSimulationV2`` (usage of class ``FMUCoSimulationV1`` is analogous):

.. code:: Python

  logging_on = False
  time_diff_resolution = 1e-9
  fmu = fmipp.FMUCoSimulationV2( uri_to_extracted_fmu, model_name, logging_on, time_diff_resolution )

  start_time = 0.
  stop_time = 10.

  instance_name = "sine_standalone1"
  visible = False
  interactive = False
  status = fmu.instantiate( instance_name, start_time, visible, interactive )
  assert status == fmipp.statusOK
    
  status = fmu.setRealValue( 'omega', 6.28318531 )
  assert status == fmipp.statusOK

  stop_time_defined = True
  status = fmu.initialize( start_time, stop_time_defined, stop_time )
  assert status == fmipp.statusOK

  time = 0.
  step_size = 1.

  while ( ( time + step_size ) - stop_time < time_diff_resolution ):
    # Make co-simulation step.
    new_step = True
    status = fmu.doStep( time, step_size, new_step )
    assert status == fmipp.statusOK

    # Advance time.
    time += step_size

	# Retrieve result.
    x = fmu.getRealValue( 'x' )
    assert fmu.getLastStatus() == fmipp.statusOK
