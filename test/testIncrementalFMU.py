
import fmipp
import os.path, math

EPS_TIME = 1e-10

work_dir = os.path.split( os.path.abspath( __file__ ) )[0] # define working directory
model_name = 'zigzag' # define FMU model name

path_to_fmu = os.path.join( work_dir, model_name + '.fmu' ) # path to FMU
uri_to_extracted_fmu = fmipp.extractFMU( path_to_fmu, work_dir ) # extract FMU

# create FMI++ wrapper for FMU for Model Exchange (Version 1.0)
fmu = fmipp.IncrementalFMU( uri_to_extracted_fmu, model_name, False, EPS_TIME )

# construct string array for init parameter names
vars = fmipp.new_string_array( 2 )
fmipp.string_array_setitem( vars, 0, 'k' )
fmipp.string_array_setitem( vars, 1, 'x' )

# construct string array for init parameter values
vals = fmipp.new_double_array( 2 )
fmipp.double_array_setitem( vals, 0, 1.0 )
fmipp.double_array_setitem( vals, 1, 0.0 )

# construct string array with output names
outputs = fmipp.new_string_array( 2 )
fmipp.string_array_setitem( outputs, 0, 'x' )
fmipp.string_array_setitem( outputs, 1, 'der(x)' )

start_time = 0.0 
step_size = 0.0025
horizon = 2*step_size
int_step_size = step_size/2

fmu.defineRealOutputs( outputs, 2 )

status = fmu.init( 'zigzag1', vars, vals, 2, start_time, horizon, step_size, int_step_size ) # initialize model
assert status == 1 # check status

result = fmu.getRealOutputs()
assert fmipp.double_array_getitem( result, 0 ) == 0.0 # check value
assert fmipp.double_array_getitem( result, 1 ) == 1.0 # check value

time = start_time
next = fmu.sync( -42.0, time )
assert next == horizon

while ( time + step_size - 1.0  < EPS_TIME ):
    oldnext = next
    next = fmu.sync( time, min( time + step_size, next ) )
    result = fmu.getRealOutputs()
    time = min( time + step_size, oldnext )
    if ( math.fabs( time - 0.5 ) < 1e-6 ):
      x = fmipp.double_array_getitem( result, 0 )
      assert math.fabs( x - 0.5 ) < 1e-4

assert math.fabs( time - 1.0 ) < step_size/2

result = fmu.getRealOutputs()
x = fmipp.double_array_getitem( result, 0 )
assert math.fabs( x - 1.0 ) < 1e-4