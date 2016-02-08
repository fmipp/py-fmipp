import fmipp
import os.path
import math

work_dir = os.path.split( os.path.abspath( __file__ ) )[0] # define working directory
model_name = 'sine_standalone' # define FMU model name

path_to_fmu = os.path.join( work_dir, model_name + '.fmu' ) # path to FMU
uri_to_extracted_fmu = fmipp.extractFMU( path_to_fmu, work_dir ) # extract FMU

logging_on = False
time_diff_resolution = 1e-9
fmu = fmipp.FMUCoSimulation( uri_to_extracted_fmu, model_name, logging_on, time_diff_resolution )

start_time = 0.
stop_time = 10.

instance_name = "sine_standalone1"
visible = False
interactive = False
status = fmu.instantiate( instance_name, start_time, visible, interactive )
assert status == fmipp.fmiOK
    
omega = 0.628318531
status = fmu.setRealValue( 'omega', omega )
assert status == fmipp.fmiOK

stop_time_defined = True
status = fmu.initialize( start_time, stop_time_defined, stop_time )
assert status == fmipp.fmiOK

time = 0.
step_size = 1.

x = 0.
cycles = 0
positive = False
twopi = 6.28318530718
    
while ( ( time + step_size ) - stop_time < time_diff_resolution ):
  # Make co-simulation step.
  new_step = True
  status = fmu.doStep( time, step_size, new_step )
  assert status == fmipp.fmiOK

  # Advance time.
  time += step_size
  assert math.fabs( time - fmu.getTime() ) < time_diff_resolution

  # Retrieve result.
  x = fmu.getRealValue( 'x' )
  assert fmu.getLastStatus() == fmipp.fmiOK

  cycles = fmu.getIntegerValue( 'cycles' )
  assert fmu.getLastStatus() == fmipp.fmiOK

  positive = fmu.getBooleanValue( 'positive' )
  assert fmu.getLastStatus() == fmipp.fmiOK

  assert math.fabs( x - math.sin( omega*time ) ) < 1e-9
  assert cycles == math.floor( omega*time/twopi )
  assert positive == ( True if ( x > 0.0 ) else False )
	
assert math.fabs( stop_time - fmu.getTime() ) < time_diff_resolution
