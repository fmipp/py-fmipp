import pytest
import os.path

import fmipp

def test_FMUModelExchange():
   work_dir = os.path.split( os.path.abspath( __file__ ) )[0] # define working directory
   model_name = 'zigzag' # define FMU model name

   path_to_fmu = os.path.join( work_dir, model_name + '.fmu' ) # path to FMU

   uri_to_extracted_fmu = fmipp.extractFMU(
      path_to_fmu, work_dir,
      command = '"C:\\Program Files\\7-Zip\\7z.exe" -o{dir} x {fmu}'
      ) # extract FMU

   # create FMI++ wrapper for FMU for Model Exchange (Version 1.0)
   logging_on = False
   stop_before_event = False
   event_search_precision = 1e-10
   integrator_type = fmipp.bdf
   fmu = fmipp.FMUModelExchangeV1(
      uri_to_extracted_fmu, model_name,
      logging_on, stop_before_event, event_search_precision, integrator_type
      )

   status = fmu.instantiate( "my_test_model_1" ) # instantiate model
   assert status == fmipp.fmiOK # check status

   status = fmu.setRealValue( 'k', 1.0 ) # set value of parameter 'k'
   assert status == fmipp.fmiOK # check status

   status = fmu.initialize() # initialize model
   assert status == fmipp.fmiOK # check status

   t = 0.0
   stepsize = 0.125
   tstop = 3.0

   x_expected = {
      0.125 : 0.125,
      0.250 : 0.250,
      0.375 : 0.375,
      0.500 : 0.500,
      0.625 : 0.625,
      0.750 : 0.750,
      0.875 : 0.875,
      1.000 : 1.000,
      1.000 : 1.000,
      1.125 : 0.875,
      1.250 : 0.750,
      1.375 : 0.625,
      1.500 : 0.500,
      1.625 : 0.375,
      1.750 : 0.250,
      1.875 : 0.125,
      2.000 : 0.000,
      2.125 : -0.125,
      2.250 : -0.250,
      2.375 : -0.375,
      2.500 : -0.500,
      2.625 : -0.625,
      2.750 : -0.750,
      2.875 : -0.875,
      3.000 : -1.000,
      }

   while ( ( t + stepsize ) - tstop < 1e-6 ):
      t = fmu.integrate( t + stepsize ) # integrate model
      x = fmu.getRealValue( "x" ) # retrieve output variable 'x'
      assert round( x, 3 ) == x_expected[ round( t, 3 ) ]


def test_IncrementalFMU():
   work_dir = os.path.split( os.path.abspath( __file__ ) )[0] # define working directory
   model_name = 'zigzag' # define FMU model name

   path_to_fmu = os.path.join(
      work_dir,
      model_name + '.fmu'
      ) # path to FMU

   uri_to_extracted_fmu = fmipp.extractFMU(
      path_to_fmu, work_dir,
      command = '"C:\\Program Files\\7-Zip\\7z.exe" -o{dir} x {fmu}'
      ) # extract FMU

   # create FMI++ wrapper for FMU for Model Exchange (Version 1.0)
   logging_on = False
   event_search_precision = 1e-7
   integrator_type = fmipp.bdf
   fmu = fmipp.IncrementalFMU(
      uri_to_extracted_fmu, model_name,
      logging_on, event_search_precision, integrator_type
      )

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
   horizon = 2 * step_size
   int_step_size = step_size / 2

   status = fmu.init(
      'zigzag1',
      init_vars, init_vals, n_init,
      start_time, horizon, step_size, int_step_size
      ) # initialize model
   assert status == 1 # check status

   time = start_time
   next = start_time

   x_expected = {
      0.0 : 0.0,
      0.3 : 0.3,
      0.6 : 0.6,
      0.9 : 0.9,
      1.0 : 1.0,
      1.3 : 0.7,
      1.6 : 0.4,
      1.9 : 0.1,
      2.2 : -0.2,
      2.5 : -0.5,
      2.8 : -0.8,
      3.0 : -1.0,
      3.3 : -0.7,
      3.6 : -0.4,
      3.9 : -0.1,
      4.2 : 0.2,
      4.5 : 0.5,
      4.8 : 0.8,
      }

   while ( time + step_size - stop_time  < 1e-6 ):
      oldnext = next
      next = fmu.sync( time, min( time + step_size, next ) )
      result = fmu.getRealOutputs()
      x = fmipp.double_array_getitem( result, 0 )
      time = min( time + step_size, oldnext )
      assert round( x, 1 ) == x_expected[ round( time, 1 ) ]


def test_FMUExport():
   from fmipp.export.createFMU import createFMU
   from FMUExportTest import FMUExportTestClass

   model_name = 'FMUExportTestCS' # define FMU model name

   start_values = {
      'pr_y' : 2.2, 'pr_x' : 1.1,
      'ir_y' : 2., 'ir_x' : 1.,
      'pi_y' : 3, 'pi_x' : 6,
      'ii_y' : 4, 'ii_x' : 5,
      'pb_y' : True, 'pb_x' : True,
      'ib_y' : False, 'ib_x' : True,
      # 'ps_y' : 'abc', 'ps_x' : 'def',
      # 'is_y' : 'ghi', 'is_x' : 'jkl'
   }

   optional_files = [ 'extra.dat' ]

   createFMU(
      FMUExportTestClass, model_name, fmi_version = '2',
      verbose = False, start_values = start_values, optional_files = optional_files )

   work_dir = os.path.split( os.path.abspath( __file__ ) )[0] # define working directory

   path_to_fmu = os.path.join( work_dir, model_name + '.fmu' ) # path to FMU

   uri_to_extracted_fmu = fmipp.extractFMU(
      path_to_fmu, work_dir,
      command = '"C:\\Program Files\\7-Zip\\7z.exe" -o{dir} x {fmu}'
      ) # extract FMU

   logging_on = False
   time_diff_resolution = 1e-9
   fmu = fmipp.FMUCoSimulationV2(
      uri_to_extracted_fmu, model_name,
      logging_on, time_diff_resolution
      )

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

   assert 1.1 == fmu.getRealValue( 'or_x' )
   assert fmu.getLastStatus() == fmipp.fmiOK

   assert 4.4 == fmu.getRealValue( 'or_y' )
   assert fmu.getLastStatus() == fmipp.fmiOK

   assert 30 == fmu.getIntegerValue( 'oi_x' )
   assert fmu.getLastStatus() == fmipp.fmiOK

   assert 12 == fmu.getIntegerValue( 'oi_y' )
   assert fmu.getLastStatus() == fmipp.fmiOK

   assert True == fmu.getBooleanValue( 'ob_x' )
   assert fmu.getLastStatus() == fmipp.fmiOK

   assert False == fmu.getBooleanValue( 'ob_y' )
   assert fmu.getLastStatus() == fmipp.fmiOK

   # assert 'jkldef' == fmu.getStringValue( 'os_x' )
   # assert fmu.getLastStatus() == fmipp.fmiOK

   # assert 'ghiabc' == fmu.getStringValue( 'os_y' )
   # assert fmu.getLastStatus() == fmipp.fmiOK


def test_FMUExport_debug():
   from FMUExportTest import FMUExportTestClass
   import warnings

   with warnings.catch_warnings():
      warnings.simplefilter( "ignore", category = RuntimeWarning )

      test = FMUExportTestClass()

      test.init(0.0)

      test.debugSetRealParameterValues( { 'pr_y' : 2.2, 'pr_x' : 1.1 } )
      test.debugSetRealInputValues( { 'ir_y' : 2., 'ir_x' : 1. } )

      test.debugSetIntegerParameterValues( { 'pi_y' : 3, 'pi_x' : 6 } )
      test.debugSetIntegerInputValues( { 'ii_y' : 4, 'ii_x' : 5 } )

      test.debugSetBooleanParameterValues( { 'pb_y' : True, 'pb_x' : True } )
      test.debugSetBooleanInputValues( { 'ib_y' : False, 'ib_x' : True } )

      test.debugSetStringParameterValues( { 'ps_y' : 'abc', 'ps_x' : 'def' } )
      test.debugSetStringInputValues( { 'is_y' : 'ghi', 'is_x' : 'jkl' } )

      test.doStep(0., 1.)

      outr = test.debugGetRealOutputValues()
      assert 1.1 == outr[ 'or_x' ]
      assert 4.4 == outr[ 'or_y' ]

      outi = test.debugGetIntegerOutputValues()
      assert 30 == outi[ 'oi_x' ]
      assert 12 == outi[ 'oi_y' ]

      outb = test.debugGetBooleanOutputValues()
      assert True == outb[ 'ob_x' ]
      assert False == outb[ 'ob_y' ]

      # outs = test.debugGetStringOutputValues()
      # assert 'jkldef' == outs[ 'os_x' ]
      # assert 'ghiabc' == outs[ 'os_y' ]
