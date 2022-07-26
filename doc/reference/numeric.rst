Module fmipp.numeric
====================

.. py:function:: getDerivatives(fmu_me)

   Extract the derivatives matrix (as ``numpy`` array) from an FMU for ModelExchange (FMI v1.0 or FMI 2.0).

   :param fmu_me: Python wrapper for FMU for ModelExchange
   :type fmu_me: FMUModelExchangeV1 or FMUModelExchangeV2   
   :return: derivatives matrix
   :rytpe: ``numpy.array``


.. py:function:: getJacobian( fmu2_me )

   Extract the Jacobian matrix (as ``numpy.array``) from an FMU for ModelExchange (FMI v2.0).

   :param FMUModelExchangeV2 fmu2_me: Python wrapper for FMU for ModelExchange (FMI v2.0)
   :return: Jacobian matrix
   :rytpe: ``numpy.array``
