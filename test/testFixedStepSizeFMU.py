import fmipp
import os.path
import math

work_dir = os.path.split( os.path.abspath( __file__ ) )[0] # define working directory
model_name = 'sine_standalone' # define FMU model name

path_to_fmu = os.path.join( work_dir, model_name + '.fmu' ) # path to FMU
uri_to_extracted_fmu = fmipp.extractFMU( path_to_fmu, work_dir ) # extract FMU

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
  reference = math.sin( 0.1 * math.pi * fmu_step_size * math.floor( time / fmu_step_size ) )
  assert math.fabs( fmipp.double_array_getitem( result, 0 ) - reference ) < 1e-8 # check value


