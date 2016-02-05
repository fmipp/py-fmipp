***************************************
The FMI++ Python Interface for Windows
***************************************

About
===============

The `Functional Mock-up Interface <https://fmi-standard.org/>`_ (FMI) specification intentionally provides only the most essential and fundamental functionalities in the form of a C interface. On the one hand, this increases flexibility in use and portability to virtually any platform. On the other hand, such a low-level approach implies several prerequisites a simulation tool has to fulfil in order to be able
to utilize such an FMI component.

This package is a Python wrapper for the `FMI++ Library <http://fmipp.sourceforge.net>`_, which intends to bridge the gap between the basic fuctionality provided by the FMI specification and the typical requirements of simulation tools. The FMI++ Library provides high-level functionalities that ease the handling and manipulation of FMUs, such as numerical integration, advanced event-handling or state predictions. This allows FMUs to be integrated more easily, e.g., into fixed time step or discrete event simulations.


Dependencies
===============

In order to provide a reliable, stable and portable solution, the FMI++ Library relies on other state-of-the-art tools where necessary. Especially, it depends upon

- the `Boost library <http://www.boost.org/>`_ (especially the `ODEINT library <http://www.odeint.com/>`_) and 
- the `SUNDIALS <https://computation.llnl.gov/casc/sundials/>`_ numerical integrator package.

Details on the licenses of the FMI++ library, Boost and SUNDIALS can be retrieved via:

.. code:: Python

  import fmipp
  fmipp.licenseInfo()


Example Usage
===============

More extensive information on the usage of can be found in the documentation of the `FMI++ Library <http://fmipp.sourceforge.net>`_.

The following gives a simple example of using an FMU for Model Exchange in a fixed time step simulation:

.. code:: Python

  import fmipp
  import os.path

  work_dir = 'C:\\path\\to\\my\\work\\dir' # define working directory (contains the FMU)
  model_name = 'MyTestModel' # define FMU model name

  path_to_fmu = os.path.join( work_dir, model_name + '.fmu' ) # path to FMU
  uri_to_extracted_fmu = fmipp.extractFMU( path_to_fmu, work_dir ) # extract FMU

  # create FMI++ wrapper for FMU for Model Exchange (Version 1.0)
  logging_on = False # no debug messages
  stop_before_event = False # do not stop integration when an event occurs
  event_search_precision = 1e-10 # precision for detecting events
  fmu = fmipp.FMUModelExchangeV1( uri_to_extracted_fmu, model_name, logging_on, stop_before_event, event_search_precision )

  status = fmu.instantiate( "my_test_model_1" ) # instantiate model
  assert status == fmipp.fmiOK # check status

  status = fmu.setRealValue( 'k', 1.0 ) # set value of parameter 'k'
  assert status == fmipp.fmiOK # check status

  status = fmu.initialize() # initialize model
  assert status == fmipp.fmiOK # check status

  t = 0.0
  stepsize = 0.125
  tstop = 1.0

  while ( ( t + stepsize ) - tstop < 1e-6 ):
    t = fmu.integrate( t + stepsize ) # integrate model
    x = fmu.getRealValue( "x" ) # retrieve output variable 'x'
