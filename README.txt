***************************************
The FMI++ Python Interface for Windows
***************************************

About
===============

The `Functional Mock-up Interface <https://fmi-standard.org/>`_ (FMI) specification intentionally provides only the most essential and fundamental functionalities in the form of a C interface.
On the one hand, this increases flexibility in use and portability to virtually any platform.
On the other hand, such a low-level approach implies several prerequisites a simulation tool has to fulfil in order to be able to utilize such an FMI component.

The `FMI++ Python Interface <https://pypi.python.org/pypi?:action=display&name=fmipp>`_ is a Python wrapper for the `FMI++ Library <http://fmipp.sourceforge.net>`_, which intends to bridge the gap between the basic fuctionality provided by the FMI specification and the typical requirements of simulation tools.
The FMI++ Library provides high-level functionalities that ease the handling and manipulation of FMUs, such as numerical integration, advanced event-handling or state predictions.
This allows FMUs to be integrated more easily, e.g., into fixed time step or discrete event simulations.

This package provides a stand-alone version of the Python interface for the `FMI++ Library <http://fmipp.sourceforge.net>`_ for Windows.
For other operating systems, this package can be built from `source <http://sourceforge.net/p/fmipp/code/ci/master/tree/>`_.

Dependencies
===============

In order to provide a reliable, stable and portable solution, the FMI++ Library relies on other state-of-the-art tools where necessary. Especially, it depends upon

- the `Boost library <http://www.boost.org/>`_ (especially the `ODEINT library <http://www.odeint.com/>`_) and 
- the `SUNDIALS <https://computation.llnl.gov/casc/sundials/>`_ numerical integrator package.

Details on the licenses of the FMI++ Library, Boost and SUNDIALS can be retrieved via:

.. code:: Python

  import fmipp
  fmipp.licenseInfo()


Documentation
===============

The FMI++ Python Interface provides several classes that allow to manipulate FMUs for ModelExchange and for Co-Simulation.
An overview on how to use it can be found `here <http://pythonhosted.org/fmipp/>`_.
More extensive background information can be found in the documentation of the `FMI++ Library <http://fmipp.sourceforge.net>`_.