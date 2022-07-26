Module fmipp.extractFMU
=======================

.. py:function:: extractFMU(fmuFilePath, outputDirPath[, command=None])

   Extract an FMU to a folder.

   :param str fmuFilePath: path to the FMU file
   :param str outputDirPath: folder to which the FMU should be extracted
   :param str command: specify the command to unzip the FMU (see info box below)
   :type command: None or str
   :returns: URI to folder containing the extracted FMU
   :rtype: str

.. note::

   By default, Python package ``zipfile`` will be used for extracting the FMU.
   However, the command for unzipping can also be specfied explicitely.
   The command should be given as a string, using tags ``{fmu}`` and ``{dir}`` as placeholders for the FMU file path and the output directory.
   For instance:
   
     - unzip: ``unzip {fmu} -d {dir}``
     - 7-zip: ``"\Program Files\7-Zip\7z.exe" -o{dir} x {fmu}``
