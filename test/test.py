import fmipp
import os.path, sys, urlparse, urllib

# Retrieve current path.
test_dir = os.path.dirname( os.path.abspath( __file__ ) )
test_dir_uri = urlparse.urljoin( 'file:', urllib.pathname2url( test_dir ) )

eps_time = 1e-9

fmu = fmipp.FMUModelExchange( test_dir_uri + "/zigzag", "zigzag", False, False, eps_time )
status = fmu.instantiate( "zigzag1" )
assert status == fmipp.fmiOK
status = fmu.setRealValue( "k", 1.0 )
assert status == fmipp.fmiOK
status = fmu.initialize()
assert status == fmipp.fmiOK

t = 0.0
stepsize = 0.0025
tstop = 1.0

while ( ( t + stepsize ) - tstop < eps_time ):
  t = fmu.integrate( t + stepsize )
  x = fmu.getRealValue( "x" )
  assert abs( x - t ) < 1e-6

t = fmu.getTime()
assert abs( t - tstop ) < stepsize/2
x = fmu.getRealValue( "x" )
assert fmu.getLastStatus() == fmipp.fmiOK
