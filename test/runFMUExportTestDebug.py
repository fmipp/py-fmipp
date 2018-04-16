#import fmipp
import warnings
from FMUExportTest import *

        

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
    for n,v in outr.items():
        print( 'real output: name = {0}, value = {1}'.format( n, v ) )
        
    outi = test.debugGetIntegerOutputValues()
    for n,v in outi.items():
        print( 'integer output: name = {0}, value = {1}'.format( n, v ) )
        
    outb = test.debugGetBooleanOutputValues()
    for n,v in outb.items():
        print( 'boolean output: name = {0}, value = {1}'.format( n, v ) )
        
    outs = test.debugGetStringOutputValues()
    for n,v in outs.items():
        print( 'string output: name = {0}, value = {1}'.format( n, v ) )