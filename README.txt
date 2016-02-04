***************************************
The FMI++ Python Interface for Windows
***************************************

About
===============

The `Functional Mock-up Interface <https://fmi-standard.org/>`_ (FMI) specification intentionally provides only the most essential and fundamental functionalities in the form of a C interface. On the one hand, this increases flexibility in use and portability to virtually any platform. On the other hand, such a low-level approach implies several prerequisites a simulation tool has to fulfil in order to be able
to utilize such an FMI component.

This package is a Python wrapper for the `FMI++ Library <http://fmipp.sourceforge.net>`_
, which intends to bridge the gap between the basic fuctionality provided by the FMI specification and the typical requirements of simulation tools. The FMI++ Library provides high-level functionalities, which ease the handling and manipulation of FMUs, such as numerical integration, advanced event-handling or state predictions. THis allows FMUs to be integrated more easily into various popular simulation approaches, e.g., fixed time step or discrete event simulations.


Dependencies
===============

In order to provide a reliable, stable and portable solution, the FMI++ Library relies on other state-of-the-art tools where necessary. Especially, it depends upon many functionality provided by

- the `Boost library <http://www.boost.org/>`_ and 
- the `SUNDIALS <https://computation.llnl.gov/casc/sundials/>`_ numerical integrator package.


Example Usage
===============

More extensive information on the usage of can be found in the documentation of the `FMI++ Library <http://fmipp.sourceforge.net>`_.

The following gives a simple example of using an FMU for Model Exchange in a fixed-step simulation:

.. code:: Python

  import fmipp
  import urlparse, urllib

  model_name = 'MyTestModel' # define FMU model name
  path_to_fmu = 'C:\\path\\to\\my\\fmu\\MyTestModel.fmu' # path to FMU

  path_to_extract = 'C:\\path\\to\\extract\\my\\fmu\\' # path to extract FMU to
  fmipp.extractFMU( path_to_fmu, path_to_extract ) # extract FMU

  # convert path to extracted FMU to URI
  uri_to_extracted_fmu = urlparse.urljoin( 'file:', urllib.pathname2url( path_to_extract + model_name ) )

  # create FMI++ wrapper for FMUModelExchange
  fmu = fmipp.FMUModelExchange( uri_to_extracted_fmu, model_name, False, False, 1e-6 )

  status = fmu.instantiate( "my_test_model_1" ) # instantiate model
  assert status == fmipp.fmiOK # check status

  status = fmu.setRealValue( 'k', 1.0 ) # set value of parameter 'k'
  assert status == fmipp.fmiOK # check status

  status = fmu.initialize() # initialize model
  assert status == fmipp.fmiOK # check status

  t = 0.0
  stepsize = 0.0025
  tstop = 1.0

  while ( ( t + stepsize ) - tstop < 1e-6 ):
    t = fmu.integrate( t + stepsize ) # integrate model
    x = fmu.getRealValue( "x" ) # retrieve output variable 'x'