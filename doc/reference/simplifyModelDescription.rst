Module fmipp.simplifyModelDescription
=====================================

.. py:function:: simplifyFMU(fmuFileName)

   Simplify an FMU by removing all scalar variables whose causality is not defined as either ``input`` or ``output`` from its XML model description.
   Also remove type definitions that are not related to input or output types.

   :param str fmuFileName: path to FMU file

   .. note:: **Attention**: The changes applied to the FMU are permanent.


.. py:function:: simplifyModelDescription(xmlModelDescription)

   Simplify an FMU's XML model description by removing all scalar variables whose causality is not defined as either ``input`` or ``output``.
   Also remove type definitions that are not related to input or output types.

   :param str xmlModelDescription: FMU model description (XML format)
