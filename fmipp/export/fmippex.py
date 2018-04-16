# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.9
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_fmippex', [dirname(__file__)])
        except ImportError:
            import _fmippex
            return _fmippex
        if fp is not None:
            try:
                _mod = imp.load_module('_fmippex', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _fmippex = swig_import_helper()
    del swig_import_helper
else:
    import _fmippex
del version_info
try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        if _newclass:
            object.__setattr__(self, name, value)
        else:
            self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr_nondynamic(self, class_type, name, static=1):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    if (not static):
        return object.__getattr__(self, name)
    else:
        raise AttributeError(name)

def _swig_getattr(self, class_type, name):
    return _swig_getattr_nondynamic(self, class_type, name, 0)


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except __builtin__.Exception:
    class _object:
        pass
    _newclass = 0


def new_double_pointer():
    return _fmippex.new_double_pointer()
new_double_pointer = _fmippex.new_double_pointer

def copy_double_pointer(value):
    return _fmippex.copy_double_pointer(value)
copy_double_pointer = _fmippex.copy_double_pointer

def delete_double_pointer(obj):
    return _fmippex.delete_double_pointer(obj)
delete_double_pointer = _fmippex.delete_double_pointer

def double_pointer_assign(obj, value):
    return _fmippex.double_pointer_assign(obj, value)
double_pointer_assign = _fmippex.double_pointer_assign

def double_pointer_value(obj):
    return _fmippex.double_pointer_value(obj)
double_pointer_value = _fmippex.double_pointer_value

def new_int_pointer():
    return _fmippex.new_int_pointer()
new_int_pointer = _fmippex.new_int_pointer

def copy_int_pointer(value):
    return _fmippex.copy_int_pointer(value)
copy_int_pointer = _fmippex.copy_int_pointer

def delete_int_pointer(obj):
    return _fmippex.delete_int_pointer(obj)
delete_int_pointer = _fmippex.delete_int_pointer

def int_pointer_assign(obj, value):
    return _fmippex.int_pointer_assign(obj, value)
int_pointer_assign = _fmippex.int_pointer_assign

def int_pointer_value(obj):
    return _fmippex.int_pointer_value(obj)
int_pointer_value = _fmippex.int_pointer_value

def new_string_pointer():
    return _fmippex.new_string_pointer()
new_string_pointer = _fmippex.new_string_pointer

def copy_string_pointer(value):
    return _fmippex.copy_string_pointer(value)
copy_string_pointer = _fmippex.copy_string_pointer

def delete_string_pointer(obj):
    return _fmippex.delete_string_pointer(obj)
delete_string_pointer = _fmippex.delete_string_pointer

def string_pointer_assign(obj, value):
    return _fmippex.string_pointer_assign(obj, value)
string_pointer_assign = _fmippex.string_pointer_assign

def string_pointer_value(obj):
    return _fmippex.string_pointer_value(obj)
string_pointer_value = _fmippex.string_pointer_value

def new_char_pointer():
    return _fmippex.new_char_pointer()
new_char_pointer = _fmippex.new_char_pointer

def copy_char_pointer(value):
    return _fmippex.copy_char_pointer(value)
copy_char_pointer = _fmippex.copy_char_pointer

def delete_char_pointer(obj):
    return _fmippex.delete_char_pointer(obj)
delete_char_pointer = _fmippex.delete_char_pointer

def char_pointer_assign(obj, value):
    return _fmippex.char_pointer_assign(obj, value)
char_pointer_assign = _fmippex.char_pointer_assign

def char_pointer_value(obj):
    return _fmippex.char_pointer_value(obj)
char_pointer_value = _fmippex.char_pointer_value

def new_double_array(nelements):
    return _fmippex.new_double_array(nelements)
new_double_array = _fmippex.new_double_array

def delete_double_array(ary):
    return _fmippex.delete_double_array(ary)
delete_double_array = _fmippex.delete_double_array

def double_array_getitem(ary, index):
    return _fmippex.double_array_getitem(ary, index)
double_array_getitem = _fmippex.double_array_getitem

def double_array_setitem(ary, index, value):
    return _fmippex.double_array_setitem(ary, index, value)
double_array_setitem = _fmippex.double_array_setitem

def new_int_array(nelements):
    return _fmippex.new_int_array(nelements)
new_int_array = _fmippex.new_int_array

def delete_int_array(ary):
    return _fmippex.delete_int_array(ary)
delete_int_array = _fmippex.delete_int_array

def int_array_getitem(ary, index):
    return _fmippex.int_array_getitem(ary, index)
int_array_getitem = _fmippex.int_array_getitem

def int_array_setitem(ary, index, value):
    return _fmippex.int_array_setitem(ary, index, value)
int_array_setitem = _fmippex.int_array_setitem

def new_string_array(nelements):
    return _fmippex.new_string_array(nelements)
new_string_array = _fmippex.new_string_array

def delete_string_array(ary):
    return _fmippex.delete_string_array(ary)
delete_string_array = _fmippex.delete_string_array

def string_array_getitem(ary, index):
    return _fmippex.string_array_getitem(ary, index)
string_array_getitem = _fmippex.string_array_getitem

def string_array_setitem(ary, index, value):
    return _fmippex.string_array_setitem(ary, index, value)
string_array_setitem = _fmippex.string_array_setitem

def new_char_array(nelements):
    return _fmippex.new_char_array(nelements)
new_char_array = _fmippex.new_char_array

def delete_char_array(ary):
    return _fmippex.delete_char_array(ary)
delete_char_array = _fmippex.delete_char_array

def char_array_getitem(ary, index):
    return _fmippex.char_array_getitem(ary, index)
char_array_getitem = _fmippex.char_array_getitem

def char_array_setitem(ary, index, value):
    return _fmippex.char_array_setitem(ary, index, value)
char_array_setitem = _fmippex.char_array_setitem

_fmippex.fmi2TypesPlatform_swigconstant(_fmippex)
fmi2TypesPlatform = _fmippex.fmi2TypesPlatform
class fmi2EventInfo(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, fmi2EventInfo, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, fmi2EventInfo, name)
    __repr__ = _swig_repr
    __swig_setmethods__["newDiscreteStatesNeeded"] = _fmippex.fmi2EventInfo_newDiscreteStatesNeeded_set
    __swig_getmethods__["newDiscreteStatesNeeded"] = _fmippex.fmi2EventInfo_newDiscreteStatesNeeded_get
    if _newclass:
        newDiscreteStatesNeeded = _swig_property(_fmippex.fmi2EventInfo_newDiscreteStatesNeeded_get, _fmippex.fmi2EventInfo_newDiscreteStatesNeeded_set)
    __swig_setmethods__["terminateSimulation"] = _fmippex.fmi2EventInfo_terminateSimulation_set
    __swig_getmethods__["terminateSimulation"] = _fmippex.fmi2EventInfo_terminateSimulation_get
    if _newclass:
        terminateSimulation = _swig_property(_fmippex.fmi2EventInfo_terminateSimulation_get, _fmippex.fmi2EventInfo_terminateSimulation_set)
    __swig_setmethods__["nominalsOfContinuousStatesChanged"] = _fmippex.fmi2EventInfo_nominalsOfContinuousStatesChanged_set
    __swig_getmethods__["nominalsOfContinuousStatesChanged"] = _fmippex.fmi2EventInfo_nominalsOfContinuousStatesChanged_get
    if _newclass:
        nominalsOfContinuousStatesChanged = _swig_property(_fmippex.fmi2EventInfo_nominalsOfContinuousStatesChanged_get, _fmippex.fmi2EventInfo_nominalsOfContinuousStatesChanged_set)
    __swig_setmethods__["valuesOfContinuousStatesChanged"] = _fmippex.fmi2EventInfo_valuesOfContinuousStatesChanged_set
    __swig_getmethods__["valuesOfContinuousStatesChanged"] = _fmippex.fmi2EventInfo_valuesOfContinuousStatesChanged_get
    if _newclass:
        valuesOfContinuousStatesChanged = _swig_property(_fmippex.fmi2EventInfo_valuesOfContinuousStatesChanged_get, _fmippex.fmi2EventInfo_valuesOfContinuousStatesChanged_set)
    __swig_setmethods__["nextEventTimeDefined"] = _fmippex.fmi2EventInfo_nextEventTimeDefined_set
    __swig_getmethods__["nextEventTimeDefined"] = _fmippex.fmi2EventInfo_nextEventTimeDefined_get
    if _newclass:
        nextEventTimeDefined = _swig_property(_fmippex.fmi2EventInfo_nextEventTimeDefined_get, _fmippex.fmi2EventInfo_nextEventTimeDefined_set)
    __swig_setmethods__["nextEventTime"] = _fmippex.fmi2EventInfo_nextEventTime_set
    __swig_getmethods__["nextEventTime"] = _fmippex.fmi2EventInfo_nextEventTime_get
    if _newclass:
        nextEventTime = _swig_property(_fmippex.fmi2EventInfo_nextEventTime_get, _fmippex.fmi2EventInfo_nextEventTime_set)

    def __init__(self):
        this = _fmippex.new_fmi2EventInfo()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _fmippex.delete_fmi2EventInfo
    __del__ = lambda self: None
fmi2EventInfo_swigregister = _fmippex.fmi2EventInfo_swigregister
fmi2EventInfo_swigregister(fmi2EventInfo)


_fmippex.fmi2OK_swigconstant(_fmippex)
fmi2OK = _fmippex.fmi2OK

_fmippex.fmi2Warning_swigconstant(_fmippex)
fmi2Warning = _fmippex.fmi2Warning

_fmippex.fmi2Discard_swigconstant(_fmippex)
fmi2Discard = _fmippex.fmi2Discard

_fmippex.fmi2Error_swigconstant(_fmippex)
fmi2Error = _fmippex.fmi2Error

_fmippex.fmi2Fatal_swigconstant(_fmippex)
fmi2Fatal = _fmippex.fmi2Fatal

_fmippex.fmi2Pending_swigconstant(_fmippex)
fmi2Pending = _fmippex.fmi2Pending

_fmippex.fmi2ModelExchange_swigconstant(_fmippex)
fmi2ModelExchange = _fmippex.fmi2ModelExchange

_fmippex.fmi2CoSimulation_swigconstant(_fmippex)
fmi2CoSimulation = _fmippex.fmi2CoSimulation

_fmippex.fmi2DoStepStatus_swigconstant(_fmippex)
fmi2DoStepStatus = _fmippex.fmi2DoStepStatus

_fmippex.fmi2PendingStatus_swigconstant(_fmippex)
fmi2PendingStatus = _fmippex.fmi2PendingStatus

_fmippex.fmi2LastSuccessfulTime_swigconstant(_fmippex)
fmi2LastSuccessfulTime = _fmippex.fmi2LastSuccessfulTime

_fmippex.fmi2Terminated_swigconstant(_fmippex)
fmi2Terminated = _fmippex.fmi2Terminated
class FMIComponentBackEnd(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, FMIComponentBackEnd, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, FMIComponentBackEnd, name)
    __repr__ = _swig_repr

    def __init__(self):
        this = _fmippex.new_FMIComponentBackEnd()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _fmippex.delete_FMIComponentBackEnd
    __del__ = lambda self: None

    def startInitialization(self):
        return _fmippex.FMIComponentBackEnd_startInitialization(self)

    def endInitialization(self):
        return _fmippex.FMIComponentBackEnd_endInitialization(self)

    def initializeRealParameters(self, names, params, n):
        return _fmippex.FMIComponentBackEnd_initializeRealParameters(self, names, params, n)

    def initializeIntegerParameters(self, names, params, n):
        return _fmippex.FMIComponentBackEnd_initializeIntegerParameters(self, names, params, n)

    def initializeBooleanParameters(self, names, params, n):
        return _fmippex.FMIComponentBackEnd_initializeBooleanParameters(self, names, params, n)

    def initializeStringParameters(self, names, params, n):
        return _fmippex.FMIComponentBackEnd_initializeStringParameters(self, names, params, n)

    def initializeRealInputs(self, names, inputs, n):
        return _fmippex.FMIComponentBackEnd_initializeRealInputs(self, names, inputs, n)

    def initializeIntegerInputs(self, names, inputs, n):
        return _fmippex.FMIComponentBackEnd_initializeIntegerInputs(self, names, inputs, n)

    def initializeBooleanInputs(self, names, inputs, n):
        return _fmippex.FMIComponentBackEnd_initializeBooleanInputs(self, names, inputs, n)

    def initializeStringInputs(self, names, inputs, n):
        return _fmippex.FMIComponentBackEnd_initializeStringInputs(self, names, inputs, n)

    def initializeRealOutputs(self, names, outputs, n):
        return _fmippex.FMIComponentBackEnd_initializeRealOutputs(self, names, outputs, n)

    def initializeIntegerOutputs(self, names, outputs, n):
        return _fmippex.FMIComponentBackEnd_initializeIntegerOutputs(self, names, outputs, n)

    def initializeBooleanOutputs(self, names, outputs, n):
        return _fmippex.FMIComponentBackEnd_initializeBooleanOutputs(self, names, outputs, n)

    def initializeStringOutputs(self, names, outputs, n):
        return _fmippex.FMIComponentBackEnd_initializeStringOutputs(self, names, outputs, n)

    def waitForMaster(self):
        return _fmippex.FMIComponentBackEnd_waitForMaster(self)

    def signalToMaster(self):
        return _fmippex.FMIComponentBackEnd_signalToMaster(self)

    def getRealParameters(self, *args):
        return _fmippex.FMIComponentBackEnd_getRealParameters(self, *args)

    def getIntegerParameters(self, *args):
        return _fmippex.FMIComponentBackEnd_getIntegerParameters(self, *args)

    def getBooleanParameters(self, *args):
        return _fmippex.FMIComponentBackEnd_getBooleanParameters(self, *args)

    def getStringParameters(self, *args):
        return _fmippex.FMIComponentBackEnd_getStringParameters(self, *args)

    def setRealParameters(self, *args):
        return _fmippex.FMIComponentBackEnd_setRealParameters(self, *args)

    def setIntegerParameters(self, *args):
        return _fmippex.FMIComponentBackEnd_setIntegerParameters(self, *args)

    def setBooleanParameters(self, *args):
        return _fmippex.FMIComponentBackEnd_setBooleanParameters(self, *args)

    def setStringParameters(self, *args):
        return _fmippex.FMIComponentBackEnd_setStringParameters(self, *args)

    def getRealInputs(self, *args):
        return _fmippex.FMIComponentBackEnd_getRealInputs(self, *args)

    def getIntegerInputs(self, *args):
        return _fmippex.FMIComponentBackEnd_getIntegerInputs(self, *args)

    def getBooleanInputs(self, *args):
        return _fmippex.FMIComponentBackEnd_getBooleanInputs(self, *args)

    def getStringInputs(self, inputs, nInputs):
        return _fmippex.FMIComponentBackEnd_getStringInputs(self, inputs, nInputs)

    def resetRealInputs(self, *args):
        return _fmippex.FMIComponentBackEnd_resetRealInputs(self, *args)

    def resetIntegerInputs(self, *args):
        return _fmippex.FMIComponentBackEnd_resetIntegerInputs(self, *args)

    def resetBooleanInputs(self, *args):
        return _fmippex.FMIComponentBackEnd_resetBooleanInputs(self, *args)

    def resetStringInputs(self, *args):
        return _fmippex.FMIComponentBackEnd_resetStringInputs(self, *args)

    def setRealOutputs(self, *args):
        return _fmippex.FMIComponentBackEnd_setRealOutputs(self, *args)

    def setIntegerOutputs(self, *args):
        return _fmippex.FMIComponentBackEnd_setIntegerOutputs(self, *args)

    def setBooleanOutputs(self, *args):
        return _fmippex.FMIComponentBackEnd_setBooleanOutputs(self, *args)

    def setStringOutputs(self, outputs, nOutputs):
        return _fmippex.FMIComponentBackEnd_setStringOutputs(self, outputs, nOutputs)

    def enforceTimeStep(self, delta):
        return _fmippex.FMIComponentBackEnd_enforceTimeStep(self, delta)

    def rejectStep(self):
        return _fmippex.FMIComponentBackEnd_rejectStep(self)

    def logger(self, status, category, msg):
        return _fmippex.FMIComponentBackEnd_logger(self, status, category, msg)

    def getCurrentCommunicationPoint(self):
        return _fmippex.FMIComponentBackEnd_getCurrentCommunicationPoint(self)

    def getCommunicationStepSize(self):
        return _fmippex.FMIComponentBackEnd_getCommunicationStepSize(self)

    def getStopTime(self):
        return _fmippex.FMIComponentBackEnd_getStopTime(self)

    def getStopTimeDefined(self):
        return _fmippex.FMIComponentBackEnd_getStopTimeDefined(self)

    def getLogFileName(self):
        return _fmippex.FMIComponentBackEnd_getLogFileName(self)

    def getRealInputNames(self, names):
        return _fmippex.FMIComponentBackEnd_getRealInputNames(self, names)

    def getIntegerInputNames(self, names):
        return _fmippex.FMIComponentBackEnd_getIntegerInputNames(self, names)

    def getBooleanInputNames(self, names):
        return _fmippex.FMIComponentBackEnd_getBooleanInputNames(self, names)

    def getStringInputNames(self, names):
        return _fmippex.FMIComponentBackEnd_getStringInputNames(self, names)

    def getRealOutputNames(self, names):
        return _fmippex.FMIComponentBackEnd_getRealOutputNames(self, names)

    def getIntegerOutputNames(self, names):
        return _fmippex.FMIComponentBackEnd_getIntegerOutputNames(self, names)

    def getBooleanOutputNames(self, names):
        return _fmippex.FMIComponentBackEnd_getBooleanOutputNames(self, names)

    def getStringOutputNames(self, names):
        return _fmippex.FMIComponentBackEnd_getStringOutputNames(self, names)
FMIComponentBackEnd_swigregister = _fmippex.FMIComponentBackEnd_swigregister
FMIComponentBackEnd_swigregister(FMIComponentBackEnd)

# This file is compatible with both classic and new-style classes.


