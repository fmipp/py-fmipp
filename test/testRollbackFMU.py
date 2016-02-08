import fmipp
import os.path
import math

work_dir = os.path.split( os.path.abspath( __file__ ) )[0] # define working directory
model_name = 'zigzag' # define FMU model name

path_to_fmu = os.path.join( work_dir, model_name + '.fmu' ) # path to FMU
uri_to_extracted_fmu = fmipp.extractFMU( path_to_fmu, work_dir ) # extract FMU

logging_on = False
fmu = fmipp.RollbackFMU( uri_to_extracted_fmu, model_name )

instance_name = 'zigzag1'
status = fmu.instantiate( instance_name )
assert status == fmipp.fmiOK

status = fmu.setRealValue( 'k', 1.0 )
assert status == fmipp.fmiOK

status = fmu.initialize()
assert status == fmipp.fmiOK

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
  assert fmu.getLastStatus() == fmipp.fmiOK

time = fmu.getTime();
assert math.fabs( time - stop_time ) < step_size/2

x = fmu.getRealValue( 'x' )
assert fmu.getLastStatus() == fmipp.fmiOK
assert math.fabs( x - 0.5 ) < 1e-6
