from fmipp.export.FMIAdapterV2 import FMIAdapterV2
import warnings

class FMUExportTestClass( FMIAdapterV2 ):

    def init( self, currentCommunicationPoint ):
        """
        Initialize the FMU (definition of input/output variables and parameters, enforce step size).
        """
        self.defineRealParameters( 'pr_x', 'pr_y' )
        self.defineRealInputs( 'ir_x', 'ir_y' )
        self.defineRealOutputs( 'or_x', 'or_y' )

        self.defineIntegerParameters( 'pi_x', 'pi_y' )
        self.defineIntegerInputs( 'ii_x', 'ii_y' )
        self.defineIntegerOutputs( 'oi_x', 'oi_y' )

        self.defineBooleanParameters( 'pb_x', 'pb_y' )
        self.defineBooleanInputs( 'ib_x', 'ib_y' )
        self.defineBooleanOutputs( 'ob_x', 'ob_y' )

        self.defineStringParameters( 'ps_x', 'ps_y' )
        self.defineStringInputs( 'is_x', 'is_y' )
        self.defineStringOutputs( 'os_x', 'os_y' )

        
    def doStep( self, currentCommunicationPoint, communicationStepSize ):
        """
        Make a simulation step.
        """
        
        # real
        
        realParam = self.getRealParameterValues()
        for n,v in realParam.items():
            print( 'real param: name = {0}, value = {1}'.format( n, v ) )

        realInputs = self.getRealInputValues()
        for n,v in realInputs.items():
            print( 'real input: name = {0}, value = {1}'.format( n, v ) )
        
        realOutputs = {
            'or_x' : realInputs['ir_x']*realParam['pr_x'], 
            'or_y' : realInputs['ir_y']*realParam['pr_y']
            }
        
        self.setRealOutputValues( realOutputs )

        # integer
        
        
        integerParam = self.getIntegerParameterValues()
        
        for n,v in integerParam.items():
            print( 'integer param: name = {0}, value = {1}'.format( n, v ) )

        integerInputs = self.getIntegerInputValues()
        
        for n,v in integerInputs.items():
            print( 'integer input: name = {0}, value = {1}'.format( n, v ) )
            
        integerOutputs = {
            'oi_x' : integerInputs['ii_x']*integerParam['pi_x'], 
            'oi_y' : integerInputs['ii_y']*integerParam['pi_y']
            }
        self.setIntegerOutputValues( integerOutputs )

        # boolean
        
        booleanParam = self.getBooleanParameterValues()
        for n,v in booleanParam.items():
            print( 'boolean param: name = {0}, value = {1}'.format( n, v ) )

        booleanInputs = self.getBooleanInputValues()
        for n,v in booleanInputs.items():
            print( 'boolean input: name = {0}, value = {1}'.format( n, v ) )
            
        booleanOutputs = {
            'ob_x' : booleanInputs['ib_x'] or  booleanParam['pb_x'], 
            'ob_y' : booleanInputs['ib_y'] and booleanParam['pb_y']
            }
        self.setBooleanOutputValues( booleanOutputs )

        # string
        
        stringParam = self.getStringParameterValues()
        for n,v in stringParam.items():
            print( 'string param: name = {0}, value = {1}'.format( n, v ) )

        stringInputs = self.getStringInputValues()
        for n,v in stringInputs.items():
            print( 'string input: name = {0}, value = {1}'.format( n, v ) )
            
        stringOutputs = {
            'os_x' : stringInputs['is_x'] + stringParam['ps_x'], 
            'os_y' : stringInputs['is_y'] + stringParam['ps_y']
            }
        self.setStringOutputValues( stringOutputs )
      