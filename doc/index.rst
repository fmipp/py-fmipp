**************************
The FMI++ Python Interface
**************************

.. meta::
   :description lang=en: The FMI++ Library

About
=====

The `Functional Mock-up Interface <https://fmi-standard.org/>`_ (FMI) specification intentionally provides only the most essential and fundamental functionalities in the form of a C interface.
On the one hand, this increases flexibility in use and portability to virtually any platform.
On the other hand, such a low-level approach implies several prerequisites a simulation tool has to fulfil in order to be able
to utilize such an FMI component.

The `FMI++ Python Interface <https://pypi.python.org/pypi?:action=display&name=fmipp>`_ is a Python wrapper for the `FMI++ Library <https://github.com/fmipp/fmipp>`_, which intends to bridge the gap between the basic fuctionality provided by the FMI specification and the typical requirements of simulation tools.
The FMI++ Library provides high-level functionalities that ease the handling and manipulation of FMUs, such as numerical integration, advanced event-handling or state predictions.
This allows FMUs to be integrated more easily, e.g., into fixed time step or discrete event simulations.

This package provides a stand-alone version of the Python interface for the `FMI++ Library <https://github.com/fmipp/fmipp>`_ for Windows (as binary wheels) and Linux (as source distribution package).
For other operating systems, this package can be built from `source <https://github.com/fmipp/py-fmipp>`_.

Getting started
===============

The `FMI++ Python Interface <https://pypi.python.org/pypi?:action=display&name=fmipp>`_ provides several classes that allow to manipulate FMUs for ModelExchange and for Co-Simulation.
In the following, short descriptions and code snippets of the provided functionality demonstrate their usage.
More extensive background information can be found in the documentation of the `FMI++ Library <https://github.com/fmipp/fmipp>`_.

Tutorial
========

An in-depth tutorial is available `online <https://github.com/fmipp/py-fmipp-tutorial>`_.
The tutorial's demos are also available as `Code Ocean compute capsule <https://doi.org/10.24433/CO.9880202.v2>`_.

.. toctree::
   :numbered:
   :maxdepth: 2
   :caption: Getting Started

   /getting-started/installation
   /getting-started/loading
   /getting-started/model-exchange
   /getting-started/co-simulation
   /getting-started/incremental-fmu
   /getting-started/fixed-step-size-fmu
   /getting-started/rollback-fmu

.. toctree::
   :hidden:
   :maxdepth: 2
   :caption: Tutorial

   /getting-started/tutorial

.. toctree::
   :maxdepth: 2
   :caption: Reference: FMI++ Classes

   /reference/FMUModelExchangeV1
   /reference/FMUModelExchangeV2
   /reference/FMUCoSimulationV1
   /reference/FMUCoSimulationV2
   /reference/IncrementalFMU
   /reference/RollbackFMU
   /reference/FixedStepSizeFMU
   /reference/InterpolatingFixedStepSizeFMU
   /reference/VariableStepSizeFMU
   /reference/FMIAdapterBase
   /reference/FMIAdapterV2

.. toctree::
   :maxdepth: 2
   :caption: Reference: Helper Functions

   /reference/SwigPyObjects
   /reference/numeric
   /reference/extractFMU
   /reference/pathToURI
   /reference/simplifyModelDescription
   /reference/createFMU

