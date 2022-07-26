Classes FMUModelExchangeV1 and FMUModelExchangeV2
=================================================

The most obvious obstacle for using a bare FMU for ModelExchange is its lack of an integrator.
For this reason, classes :doc:`FMUModelExchangeV1 </reference/FMUModelExchangeV1>` and :doc:`FMUModelExchangeV2 </reference/FMUModelExchangeV2>` provide generic methods for the integration of FMUs for ModelExchange for FMI Version 1.0 and 2.0, respectively.
Instances of these classes own the actual FMU instance and are able to advance the current state up to a specified point in time, including the
proper handling of FMU-internal events.
The classes also provide functionality for convenient input and output handling.

The following example demonstrates the basic usage of class :doc:`FMUModelExchangeV2 </reference/FMUModelExchangeV2>` (usage of class :doc:`FMUModelExchangeV1 </reference/FMUModelExchangeV1>` is analogous):

.. code:: Python

  # create FMI++ wrapper for FMU for ModelExchange (Version 2.0)
  logging_on = False
  stop_before_event = False
  event_search_precision = 1e-10
  integrator_type = fmipp.integratorBDF
  fmu = fmipp.FMUModelExchangeV2( uri_to_extracted_fmu, model_name, logging_on, stop_before_event, event_search_precision, integrator_type )

  status = fmu.instantiate( "my_test_model_1" ) # instantiate model
  assert status == fmipp.statusOK # check status

  status = fmu.setRealValue( 'k', 1.0 ) # set value of parameter 'k'
  assert status == fmipp.statusOK # check status

  status = fmu.initialize() # initialize model
  assert status == fmipp.statusOK # check status

  t = 0.0
  stepsize = 0.125
  tstop = 3.0

  while ( ( t + stepsize ) - tstop < 1e-6 ):
    t = fmu.integrate( t + stepsize ) # integrate model
    x = fmu.getRealValue( "x" ) # retrieve output variable 'x'
	
The integration algorithms provided by ODEINT and SUNDIALS can be chosen with an appropriate flag in the constructor (see example above).
The following algorithms are available:

+----------------+----------------------------------+----------+-------+----------+------------------------------------------------+
| Stepper        | Name                             | Suite    | Order | Adaptive | Recommended usecases                           |
+----------------+----------------------------------+----------+-------+----------+------------------------------------------------+
| integratorEU   | Explicit Euler                   | ODEINT   | 1     | No       | Testing                                        |
+----------------+----------------------------------+----------+-------+----------+------------------------------------------------+
| integratorRK   | 4th order Runge-Kutta            | ODEINT   | 4     | No       | Testing                                        |
+----------------+----------------------------------+----------+-------+----------+------------------------------------------------+
| integratorABM  | Adams-Bashforth-Moulton          | ODEINT   | 8     | No       | Testing                                        |
+----------------+----------------------------------+----------+-------+----------+------------------------------------------------+
| integratorCK   | Cash-Karp                        | ODEINT   | 5     | Yes      | Nonstiff Models                                |
+----------------+----------------------------------+----------+-------+----------+------------------------------------------------+
| integratorDP   | Dormand-Prince                   | ODEINT   | 5     | Yes      | Nonstiff Models                                |
+----------------+----------------------------------+----------+-------+----------+------------------------------------------------+
| integratorFE   | Fehlberg                         | ODEINT   | 8     | Yes      | Nonstiff, smooth Models                        |
+----------------+----------------------------------+----------+-------+----------+------------------------------------------------+
| integratorBS   | Bulirsch Stoer                   | ODEINT   | 1-16  | Yes      | High precision required                        |
+----------------+----------------------------------+----------+-------+----------+------------------------------------------------+
| integratorRO   | Rosenbrock                       | ODEINT   | 4     | Yes      | Stiff Models                                   |
+----------------+----------------------------------+----------+-------+----------+------------------------------------------------+
| integratorBDF  | Backward Differentiation Formula | SUNDIALS | 1-5   | Yes      | Stiff Models                                   |
+----------------+----------------------------------+----------+-------+----------+------------------------------------------------+
| integratorABM2 | Adams-Bashforth-Moulton          | SUNDIALS | 1-12  | Yes      | Nonstiff Models with expensive right hand side |
+----------------+----------------------------------+----------+-------+----------+------------------------------------------------+


