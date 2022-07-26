Module fmipp.export.createFMU
=============================

.. py:function:: createFMU(fmu_backend, fmi_model_identifier[, fmi_version='2', verbose=False, litter=False, start_values=None, optional_files=None])

   Create an FMU for Co-Simulation for a class derived from :doc:`FMIAdapterBase </reference/FMIAdapterBase>`.
   An example of its usage is available `here <https://github.com/fmipp/py-fmipp-tutorial/blob/master/demos/TestFMUExport.ipynb>`_.

   :param fmu_backend: class implementing the abstract base class FMIAdapter (class derived from FMIAdapter) 
   :param str fmi_model_identifier: FMI model identifier
   :param str fmi_version: FMI version (``1`` or ``2``)
   :param bool verbose: turn on log messages
   :param bool litter: do not clean-up intermediate files
   :param start_values: start values may be specified for paramters and input variables
   :type start_values: None or dict
   :param optional_files: additional files (e.g., for weather data) may be specified as extra arguments; these files will be automatically copied to the resources directory of the FMU
   :type optional_files: None or list[str] 
