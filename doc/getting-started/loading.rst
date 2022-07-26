Loading the library and extracting an FMU
==========================================

FMUs are basically ZIP archives.
To load the library and extract an FMU for further processing do something like this:

.. code:: Python

  import fmipp
  import os

  work_dir = 'C:\\path\\to\\my\\work\\dir' # define working directory (contains the FMU)
  model_name = 'MyTestModel' # define FMU model name
  path_to_fmu = os.path.join( work_dir, model_name + '.fmu' ) # path to FMU

  uri_to_extracted_fmu = fmipp.extractFMU( path_to_fmu, work_dir ) # extract FMU

The last line not only extracts the FMU, but also return an URI to the extracted FMU's location.
Since all constructors of the the FMI++ Library take URIs to extracted FMUs as input arguments, this function comes in very handy.


