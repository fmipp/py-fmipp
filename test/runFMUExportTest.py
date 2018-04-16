import os
import fmipp
from fmipp.export.createFMU import createFMU
from FMUExportTest import *

model_name = 'FMUExportTestCS' # define FMU model name

start_values = { 
    'pr_y' : 2.2, 'pr_x' : 1.1,
    'ir_y' : 2., 'ir_x' : 1.,
    'pi_y' : 3, 'pi_x' : 6,
    'ii_y' : 4, 'ii_x' : 5,
    'pb_y' : True, 'pb_x' : True,
    'ib_y' : False, 'ib_x' : True,
    'ps_y' : 'abc', 'ps_x' : 'def',
    'is_y' : 'ghi', 'is_x' : 'jkl' 
    }

optional_files = [ 'extra.dat' ]

createFMU( FMUExportTestClass, model_name, fmi_version = '2', verbose = True, start_values = start_values, optional_files = optional_files )


work_dir = os.path.split( os.path.abspath( __file__ ) )[0] # define working directory

path_to_fmu = os.path.join( work_dir, model_name + '.fmu' ) # path to FMU

uri_to_extracted_fmu = fmipp.extractFMU( path_to_fmu, work_dir ) # extract FMU

logging_on = True
time_diff_resolution = 1e-9
fmu = fmipp.FMUCoSimulationV2( uri_to_extracted_fmu, model_name, logging_on, time_diff_resolution )

start_time = 0.
stop_time = 10.

instance_name = "test1"
visible = False
interactive = False
status = fmu.instantiate( instance_name, start_time, visible, interactive )
assert status == fmipp.fmiOK

stop_time_defined = True
status = fmu.initialize( start_time, stop_time_defined, stop_time )
assert status == fmipp.fmiOK

time = 0.
step_size = 1.

new_step = True
status = fmu.doStep( time, step_size, new_step )
assert status == fmipp.fmiOK

print( 'or_x = {}'.format( fmu.getRealValue( 'or_x' ) ) )
assert fmu.getLastStatus() == fmipp.fmiOK

print( 'or_y = {}'.format( fmu.getRealValue( 'or_y' ) ) )
assert fmu.getLastStatus() == fmipp.fmiOK

print( 'oi_x = {}'.format( fmu.getIntegerValue( 'oi_x' ) ) )
assert fmu.getLastStatus() == fmipp.fmiOK

print( 'oi_y = {}'.format( fmu.getIntegerValue( 'oi_y' ) ) )
assert fmu.getLastStatus() == fmipp.fmiOK

print( 'ob_x = {}'.format( fmu.getBooleanValue( 'ob_x' ) ) )
assert fmu.getLastStatus() == fmipp.fmiOK

print( 'ob_y = {}'.format( fmu.getBooleanValue( 'ob_y' ) ) )
assert fmu.getLastStatus() == fmipp.fmiOK

print( 'os_x = {}'.format( fmu.getStringValue( 'os_x' ) ) )
assert fmu.getLastStatus() == fmipp.fmiOK

print( 'os_y = {}'.format( fmu.getStringValue( 'os_y' ) ) )
assert fmu.getLastStatus() == fmipp.fmiOK
