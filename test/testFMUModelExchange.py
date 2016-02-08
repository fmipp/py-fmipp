
import fmipp
import os.path

work_dir = os.path.split( os.path.abspath( __file__ ) )[0] # define working directory
model_name = 'zigzag' # define FMU model name

path_to_fmu = os.path.join( work_dir, model_name + '.fmu' ) # path to FMU
uri_to_extracted_fmu = fmipp.extractFMU( path_to_fmu, work_dir ) # extract FMU

# create FMI++ wrapper for FMU for Model Exchange (Version 1.0)
logging_on = False
stop_before_event = False
event_search_precision = 1e-10
integrator_type = fmipp.bdf
fmu = fmipp.FMUModelExchangeV1( uri_to_extracted_fmu, model_name, logging_on, stop_before_event, event_search_precision, integrator_type )

status = fmu.instantiate( "my_test_model_1" ) # instantiate model
assert status == fmipp.fmiOK # check status

status = fmu.setRealValue( 'k', 1.0 ) # set value of parameter 'k'
assert status == fmipp.fmiOK # check status

status = fmu.initialize() # initialize model
assert status == fmipp.fmiOK # check status

t = 0.0
stepsize = 0.125
tstop = 3.0

while ( ( t + stepsize ) - tstop < 1e-6 ):
  t = fmu.integrate( t + stepsize ) # integrate model
  x = fmu.getRealValue( "x" ) # retrieve output variable 'x'
  print "t = {:2.3f} - x = {:2.3f}".format( t, x )
