# -----------------------------------------------------------------
# Copyright (c) 2022, AIT Austrian Institute of Technology GmbH.
# All rights reserved. See file FMIPP_LICENSE.txt for details.
# -----------------------------------------------------------------

try:

    import numpy as np

    def _get_item( a, i ):
        return double_array_getitem( a, i )

    def getDerivatives( fmu_me ):
        '''
        Extract the derivatives matrix (as numpy.array) from an FMU for ModelExchange (FMI v1.0 or FMI 2.0).
        '''

        if not isinstance( fmu_me, FMUModelExchangeV1 ) and not isinstance( fmu_me, FMUModelExchangeV2 ):
            raise TypeError( 'this function is only supported for FMUModelExchangeV1 and FMUModelExchangeV2' )

        n = fmu_me.nStates()
        der = new_double_array( n )
        fmu_me.getDerivatives( der )

        return np.array( [ _get_item(der, i) for i in range(0, n) ] )

    def getJacobian( fmu2_me ):
        '''
        Extract the Jacobian matrix (as numpy.array) from an FMU for ModelExchange (FMI v2.0).
        '''

        if not isinstance( fmu2_me, FMUModelExchangeV2 ):
            raise TypeError( 'this function is only supported for FMUModelExchangeV2' )

        n = fmu2_me.nStates()
        jac = new_double_array( n * n )
        fmu2_me.getJac( jac )

        return np.array( [ [ _get_item(jac, i) for i in range(j*n, (j+1)*n)] for j in range(0, n) ] )

except ModuleNotFoundError:

    print( 'Unable to load fmipp.numeric. Probably numpy is not installed?' )
