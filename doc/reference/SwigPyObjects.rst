C/C++ array wrappers
====================

Several classes of package ``fmipp`` use objects of type ``SwigPyObject`` as inputs and outputs, which are wrappers around C/C++ arrays.
Instantiation of and data access to these objects should be done via the helper functions listed here.

.. rubric:: Methods for creating array wrappers
   :name: methods_new_array

These helper functions create new C/C++ arrays in memory and return a Python wrapper object to this array.

.. py:function:: new_bool_pointer(nelements)

   :param int nelements: size of array 
   :rtype: SwigPyObject (wrapper for array of type ``bool``)

.. py:function:: new_double_array(nelements)

   :param int nelements: size of array 
   :rtype: SwigPyObject (wrapper for array of type ``float``)

.. py:function:: new_int_array(nelements)

   :param int nelements: size of array 
   :rtype: SwigPyObject (wrapper for array of type ``int``)

.. py:function:: new_string_array(nelements)

   :param int nelements: size of array 
   :rtype: SwigPyObject (wrapper for array of type ``str``)


.. rubric:: Methods for retrieving array element values
   :name: methods_getitem_array

.. note:: Indexing starts at 0.

These helper functions return the value of array elements.

.. py:function:: bool_array_getitem(ary, index)

   :param SwigPyObject ary: array wrapper object
   :param int index: element index
   :rtype: bool

.. py:function:: double_array_getitem(ary, index)

   :param SwigPyObject ary: array wrapper object
   :param int index: element index
   :rtype: float

.. py:function:: int_array_getitem(ary, index)

   :param SwigPyObject ary: array wrapper object
   :param int index: element index
   :rtype: int

.. py:function:: string_array_getitem(ary, index)

   :param SwigPyObject ary: array wrapper object
   :param int index: element index
   :rtype: str

 
.. rubric:: Methods for setting array element values
   :name: methods_setitem_array

These helper functions set the value of array elements.

.. note:: Indexing starts at 0.
 
.. py:function:: bool_array_setitem(ary, index, value)

   :param SwigPyObject ary: array wrapper object
   :param int index: element index
   :param bool value: new element value 

.. py:function:: double_array_setitem(ary, index, value)

   :param SwigPyObject ary: array wrapper object
   :param int index: element index
   :param float value: new element value 

.. py:function:: int_array_setitem(ary, index, value)

   :param SwigPyObject ary: array wrapper object
   :param int index: element index
   :param int value: new element value 

.. py:function:: string_array_setitem(ary, index, value)

   :param SwigPyObject ary: array wrapper object
   :param int index: element index
   :param str value: new element value 


.. rubric:: Methods for deleting arrays
   :name: methods_delete_array

These helper functions delete an array wrapper object and release the corresponding space in memory.
 
.. py:function:: delete_bool_array(ary)

   :param SwigPyObject ary: array wrapper object

.. py:function:: delete_double_array(ary)

   :param SwigPyObject ary: array wrapper object

.. py:function:: delete_int_array(ary)

   :param SwigPyObject ary: array wrapper object

.. py:function:: delete_string_array(ary)

   :param SwigPyObject ary: array wrapper object
