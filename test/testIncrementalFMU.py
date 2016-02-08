
import fmipp
import os.path, math

work_dir = os.path.split( os.path.abspath( __file__ ) )[0] # define working directory
model_name = 'zigzag' # define FMU model name

path_to_fmu = os.path.join( work_dir, model_name + '.fmu' ) # path to FMU
uri_to_extracted_fmu = fmipp.extractFMU( path_to_fmu, work_dir ) # extract FMU

# create FMI++ wrapper for FMU for Model Exchange (Version 1.0)
logging_on = False
event_search_precision = 1e-7
integrator_type = fmipp.rk
fmu = fmipp.IncrementalFMU( uri_to_extracted_fmu, model_name, logging_on, event_search_precision, integrator_type )

# number of parameters that should be initialized
n_init = 2

# construct string array for init parameter names
init_vars = fmipp.new_string_array( n_init )
fmipp.string_array_setitem( init_vars, 0, 'k' )
fmipp.string_array_setitem( init_vars, 1, 'x' )

# construct string array for init parameter values
init_vals = fmipp.new_double_array( n_init )
fmipp.double_array_setitem( init_vals, 0, 1.0 )
fmipp.double_array_setitem( init_vals, 1, 0.0 )

# define number of real outputs
n_real_outputs = 1

# construct string array with output names
outputs = fmipp.new_string_array( n_real_outputs )
fmipp.string_array_setitem( outputs, 0, 'x' )

# define real outputs
fmu.defineRealOutputs( outputs, n_real_outputs )

start_time = 0.0
stop_time = 5.0
step_size = 0.3
horizon = 2*step_size
int_step_size = step_size/2

status = fmu.init( 'zigzag1', init_vars, init_vals, n_init, start_time, horizon, step_size, int_step_size ) # initialize model
assert status == 1 # check status

time = start_time
next = start_time

while ( time + step_size - stop_time  < 1e-6 ):
  oldnext = next
  next = fmu.sync( time, min( time + step_size, next ) )
  result = fmu.getRealOutputs()
  time = min( time + step_size, oldnext )
  print "t = {:1.2f} - x = {:1.2f}".format( time, fmipp.double_array_getitem( result, 0 ) )

