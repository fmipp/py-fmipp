# -----------------------------------------------------------------
# Copyright (c) 2022, AIT Austrian Institute of Technology GmbH.
# All rights reserved. See file FMIPP_LICENSE.txt for details.
# -----------------------------------------------------------------

#
# This file is used to create FMUs for Co-Simulation from Python code.
#

### Setup for Python 2.
try:
    import sys, os, shutil, time, getpass, uuid, pickle, subprocess, glob, urlparse, urllib, collections, inspect, warnings, platform
except:
    pass

### Setup for Python 3.
try:
    import sys, os, shutil, time, getpass, uuid, pickle, subprocess, glob, urllib.parse as urlparse, urllib.request as urllib, collections, inspect, warnings, platform
except:
    pass

def log( *arg ):
    print( ' '.join( map( str, arg ) ) )
    sys.stdout.flush()


from fmipp.export.FMIAdapterBase import FMIAdapterBase
from fmipp.export.fmi1 import *
from fmipp.export.fmi2 import *

def createFMU(
    fmu_backend,
    fmi_model_identifier,
    fmi_version = '2',
    verbose = False,
    litter = False,
    start_values = None,
    optional_files = None ):
    """
    Create and FMU for Co-Simulation for a class derived from FMIAdapter.

    :param fmu_backend: class implementing the abstract base class FMIAdapter (class derived from FMIAdapter)
    :param fmi_model_identifier: FMI model identifier (str)
    :param fmi_version: FMI version (str, 1 or 2, default: 2)
    :param verbose: turn on log messages (boolean, default: False)
    :param litter: do not clean-up intermediate files (boolean, default: False)
    :param start_values: start values may be specified for paramters and input variables (None or dict, default: None)
    :param optional_files: additional files (e.g., for weather data) may be specified as extra arguments; these files will be automatically copied to the resources directory of the FMU (None or list of str, default: None)
    """

    # Check FMI model identifier.
    if not isinstance( fmi_model_identifier, str ):
        raise TypeError( 'parameter \'fmi_model_identifier\' must be of type \'str\'' )

    # Check FMI model identifier.
    if not fmi_version in [ '1', '2' ]:
        raise TypeError( 'parameter \'fmi_version\' must be either 1 or 2' )

    # Check verbosity flag.
    if not isinstance( verbose, bool ):
        raise TypeError( 'parameter \'verbose\' must be of type \'bool\'' )

    # Check verbosity flag.
    if not isinstance( litter, bool ):
        raise TypeError( 'parameter \'litter\' must be of type \'bool\'' )

    # Check start values.
    if start_values is None:
        start_values = {}
    elif not isinstance( start_values, dict ):
        raise TypeError( 'parameter \'start_values\' must be \'None\' or of type \'dict\'' )

    # Check optional files.
    if optional_files is None:
        optional_files = []
    elif not isinstance( optional_files, list ) and not all( isinstance( elem, str ) for elem in optional_files ):
        raise TypeError( 'parameter \'optional_files\' must be \'None\' or of type \'list of str\'' )

    # Create container for all used Python modules, which will be passed to all called functions.
    # This makes it easier to run this script with different Python version (2.x and 3.x).
    Modules = collections.namedtuple( 'Modules', [ 'sys', 'os', 'shutil', 'time', 'getpass', 'uuid', 'urlparse', 'urllib', 'pickle', 'subprocess', 'glob', 'log', 'inspect', 'warnings', 'platform' ] )
    modules = Modules( sys, os, shutil, time, getpass, uuid, urlparse, urllib, pickle, subprocess, glob, log, inspect, warnings, platform )

    if ( True == verbose ):
        modules.log( '[DEBUG] Using FMI version {}'.format( fmi_version ) )
        modules.log( '[DEBUG] FMI model identifier: {}'.format( fmi_model_identifier ) )
        modules.log( '[DEBUG] Aditional files:' )
        for file_name in optional_files:
            modules.log( '\t{}'.format( file_name ) )

    # Inspect implementation of FMU back-end to retrieve FMI input and output variable names.
    ( fmi_input_vars, fmi_output_vars, fmi_parameters, fmu_backend_class, fmu_backend_file ) = inspectFMUBackend( fmu_backend, verbose, modules )

    try:
        fmu_name = generateFMU(
            fmi_version,
            fmi_model_identifier,
            fmu_backend_class,
            fmu_backend_file,
            fmi_input_vars,
            fmi_output_vars,
            fmi_parameters,
            start_values,
            optional_files,
            verbose,
            litter,
            modules )

        if ( True == verbose ): modules.log( "[DEBUG] FMU created successfully:", fmu_name )

    except Exception as e:
        modules.log( e )
        modules.sys.exit( e.args[0] )


def inspectFMUBackend( fmu_backend, verbose, modules ):
    """
    Check if backend inherits from FMIAdapter.
    Retrieve the name of the file in which the backend is defined.
    Retrieve the input variables, output variables and parameter that an FMU backend implementation defines.
    """
    # Check FMU backend implementation.
    if not issubclass( fmu_backend, FMIAdapterBase ):
        raise TypeError( 'class \'fmu_backend\' must be a subclass of \'FMIAdapter\'' )

    # Dicts containing information about the FMI input variables, output variables and parameters.
    fmi_input_vars = {}
    fmi_output_vars = {}
    fmi_parameters = {}

    # Instantiate the backend (debug mode).
    backend = fmu_backend()

    fmu_backend_class = backend.__class__.__name__

    # Get file in which the backend class is defined.
    fmu_backend_file = str()
    try:
        fmu_backend_file = modules.inspect.getsourcefile( backend.__class__ )

        if ( True is verbose ):
            modules.log( '[DEBUG] Class \'{0}\' defined in file: {1}'.format( fmu_backend_class, fmu_backend_file ) )
    except TypeError:
        raise RuntimeError( 'File containing definition of class \'{}\' not found'.format( fmu_backend_class )  )

    with modules.warnings.catch_warnings():
        modules.warnings.simplefilter( "ignore", category = RuntimeWarning )
        # Initialize the backend.
        backend.init( 0 )

        fmi_input_vars[ 'Real' ] = backend._realInputNames
        fmi_input_vars[ 'Integer' ] = backend._integerInputNames
        fmi_input_vars[ 'Boolean' ] = backend._booleanInputNames
        fmi_input_vars[ 'String' ] = backend._stringInputNames

        if ( True == verbose ):
            modules.log( '[DEBUG] FMI input variables:' )
            for type, vars in fmi_input_vars.items():
                for var in vars:
                    modules.log( '\t{0} ({1})'.format( var, type ) )

        fmi_output_vars[ 'Real' ] = backend._realOutputNames
        fmi_output_vars[ 'Integer' ] = backend._integerOutputNames
        fmi_output_vars[ 'Boolean' ] = backend._booleanOutputNames
        fmi_output_vars[ 'String' ] = backend._stringOutputNames

        if ( True == verbose ):
            modules.log( '[DEBUG] FMI output variables:' )
            for type, vars in fmi_output_vars.items():
                for var in vars:
                    modules.log( '\t{0} ({1})'.format( var, type ) )

        fmi_parameters[ 'Real' ] = backend._realParameterNames
        fmi_parameters[ 'Integer' ] = backend._integerParameterNames
        fmi_parameters[ 'Boolean' ] = backend._booleanParameterNames
        fmi_parameters[ 'String' ] = backend._stringParameterNames

        if ( True == verbose ):
            modules.log( '[DEBUG] FMI parameters:' )
            for type, vars in fmi_parameters.items():
                for var in vars:
                    modules.log( '\t{0} ({1})'.format( var, type ) )

    return ( fmi_input_vars, fmi_output_vars, fmi_parameters, fmu_backend_class, fmu_backend_file )


def generateFMU(
    fmi_version,
    fmi_model_identifier,
    fmu_backend_class,
    fmu_backend_file,
    fmi_input_vars,
    fmi_output_vars,
    fmi_parameters,
    start_values,
    optional_files,
    verbose,
    litter,
    modules ):
    """
    Generate an FMU from Python code.

    :param fmi_version: FMI version
    :param fmi_model_identifier: FMI model identfier for FMU
    :param fmu_backend_class: name of the backend class
    :param fmu_backend_file: file defining the backend class
    :param fmi_input_vars: definition of input variables
    :param fmi_output_vars: definition of output variable names
    :param start_values: definition of start values
    :param optional_files: definition of additional files
    :param verbose: verbosity flag
    :param litter: do not clean-up intermediate files
    :param modules: named tuple containing all imported modules
    """
    # Create new GUID.
    guid = str( modules.uuid.uuid1() )

    # Create FMU model description.
    model_description_name = createModelDescription( fmi_version, fmi_model_identifier, fmu_backend_class, fmu_backend_file, fmi_input_vars, fmi_output_vars, fmi_parameters, guid, start_values, optional_files, verbose, modules )

    # Create script for running the backend implementation.
    backend_script_name = createBackendScript( fmu_backend_class, fmu_backend_file, guid, verbose, modules )

    # Create FMU shared library.
    fmu_shared_library_name = createSharedLibrary( fmi_model_identifier, fmi_version, verbose, modules )

    # Check if working directory for FMU creation already exists.
    if ( True == modules.os.path.isdir( fmi_model_identifier ) ):
        modules.shutil.rmtree( fmi_model_identifier, False )

    # Retrieve platform information.
    platform_type = str()
    platform_id = modules.platform.platform().lower()
    platform_bits = modules.platform.architecture()[0][:2]
    if 'linux' in platform_id:
        platform_type = 'linux' + platform_bits
    elif 'cygwin' in platform_id:
        platform_type = 'cygwin' + platform_bits
    elif 'windows' in platform_id:
        platform_type = 'win' + platform_bits
    else:
        raise RuntimeError( '\n[ERROR] platform not supported: {}'.format( modules.platform.platform() ) )

    # Working directory path for the FMU DLL.
    binaries_dir = modules.os.path.join( fmi_model_identifier, 'binaries', platform_type )

    # Create working directory (incl. sub-directories) for FMU creation.
    modules.os.makedirs( binaries_dir )

    # Resources directory path.
    resources_dir = modules.os.path.join( fmi_model_identifier, 'resources' )

    # Create resources directory for FMU creation.
    modules.os.makedirs( resources_dir )

    # Copy all files to working directory.
    modules.shutil.copy( model_description_name, fmi_model_identifier ) # XML model description.
    modules.shutil.copy( backend_script_name, resources_dir ) # Script for running the backend implementation.
    modules.shutil.copy( fmu_backend_file, resources_dir ) # backend implementation.
    for file_name in optional_files: # Additional files.
        modules.shutil.copy( file_name, resources_dir )
    modules.shutil.copy( fmu_shared_library_name, binaries_dir ) # FMU DLL.

    # Create ZIP archive.
    if ( True == modules.os.path.isfile( fmi_model_identifier + '.zip' ) ):
        modules.os.remove( fmi_model_identifier + '.zip' )
    modules.shutil.make_archive( fmi_model_identifier, 'zip', fmi_model_identifier )

    # Finally, create the FMU!!!
    fmu_file_name = fmi_model_identifier + '.fmu'
    if ( True == modules.os.path.isfile( fmu_file_name ) ):
        modules.os.remove( fmu_file_name )
    modules.os.rename( fmi_model_identifier + '.zip', fmu_file_name )

    # Clean up.
    if ( False == litter ):
        for fn in [ model_description_name, backend_script_name, 'build.log', 'fmiFunctions.obj' ]:
            modules.os.remove( fn ) if modules.os.path.isfile( fn ) else None
        modules.shutil.rmtree( fmi_model_identifier, False )
        for file_name in modules.glob.glob( fmi_model_identifier + '.*' ):
            if not ( '.fmu' in file_name or '.py' in file_name ): modules.os.remove( file_name )

    # Return name of created FMU.
    return fmu_file_name


# Create model description.
def createModelDescription(
        fmi_version,
        fmi_model_identifier,
        fmu_backend_class,
        fmu_backend_file,
        fmi_input_vars,
        fmi_output_vars,
        fmi_parameters,
        guid,
        start_values,
        optional_files,
        verbose,
        modules ):
    # Retrieve templates for different parts of XML model description according to FMI version.
    ( model_description_header, scalar_variable_node, model_description_footer ) = getModelDescriptionTemplates( fmi_version, verbose, modules )

    # FMI model identifier.
    model_description_header = model_description_header.replace( '__MODEL_IDENTIFIER__', fmi_model_identifier )

    # Model name.
    fmi_model_name = modules.os.path.basename( fmu_backend_file ).split( '.' )[0] # Deck file name with extension.
    model_description_header = model_description_header.replace( '__MODEL_NAME__', fmi_model_name )

    # Creation date and time.
    model_description_header = model_description_header.replace( '__DATE_AND_TIME__', modules.time.strftime( "%Y-%m-%dT%H:%M:%S" ) )

    # Author name.
    model_description_header = model_description_header.replace( '__USER__', modules.getpass.getuser() )

    # GUID.
    model_description_header = model_description_header.replace( '__GUID__', guid )

    # URI of Python main executable.
    python_exe_uri = modules.urlparse.urljoin( 'file:', modules.urllib.pathname2url( modules.sys.executable ) )
    model_description_header = model_description_header.replace( '__PYTHON_URI__', python_exe_uri )

    # Define a string to collect all scalar variable definitions.
    model_description_scalars = ''

    # Add scalar input variables description. Value references for inputs start with 1.
    input_val_ref = 1
    for type, vars in fmi_input_vars.items():
        for var in vars:
            scalar_variable_description = scalar_variable_node
            scalar_variable_description = addVariabilityAndCausalityToModelDescription( scalar_variable_description, fmi_version, type, True, False, verbose, modules )
            scalar_variable_description = scalar_variable_description.replace( '__VAR_TYPE__', type )
            scalar_variable_description = scalar_variable_description.replace( '__VAR_NAME__', var )
            scalar_variable_description = scalar_variable_description.replace( '__VAL_REF__', str( input_val_ref ) )
            scalar_variable_description = scalar_variable_description.replace( '__INITIAL__', '' )
            if var in start_values:
                if isinstance( start_values[var], bool ): start_values[var] = int( start_values[var] )
                start_value_description = ' start=\"' + str( start_values[var] ) + '\"'
                scalar_variable_description = scalar_variable_description.replace( '__START_VALUE__', start_value_description )
                if ( True == verbose ): modules.log( '[DEBUG] Added start value to model description: ', var, '=', start_values[var] )
            else:
                scalar_variable_description = scalar_variable_description.replace( '__START_VALUE__', '' )
            input_val_ref += 1
            # Write scalar variable description to file.
            model_description_scalars += scalar_variable_description;

    # Add scalar input variables description. Value references for outputs start with 1001 (except there are already input value references with corresponding values).
    output_val_ref = 1001 if ( input_val_ref < 1001 ) else input_val_ref
    for type, vars in fmi_output_vars.items():
        for var in vars:
            scalar_variable_description = scalar_variable_node
            scalar_variable_description = addVariabilityAndCausalityToModelDescription( scalar_variable_description, fmi_version, type, False, False, verbose, modules )
            scalar_variable_description = scalar_variable_description.replace( '__VAR_TYPE__', type )
            scalar_variable_description = scalar_variable_description.replace( '__VAR_NAME__', var )
            scalar_variable_description = scalar_variable_description.replace( '__VAL_REF__', str( output_val_ref ) )
            if var in start_values:
                if isinstance( start_values[var], bool ): start_values[var] = int( start_values[var] )
                start_value_description = ' start=\"' + str( start_values[var] ) + '\"'
                scalar_variable_description = scalar_variable_description.replace( '__START_VALUE__', start_value_description )
                scalar_variable_description = scalar_variable_description.replace( '__INITIAL__', 'initial="exact"' )
                if ( True == verbose ): modules.log( '[DEBUG] Added start value to model description: ', var, '=', start_values[var] )
            else:
                scalar_variable_description = scalar_variable_description.replace( '__START_VALUE__', '' )
                scalar_variable_description = scalar_variable_description.replace( '__INITIAL__', '' )
            output_val_ref += 1
            # Write scalar variable description to file.
            model_description_scalars += scalar_variable_description;

    # Add parameter descriptions. Value references for parameters start with 2001 (except there are already other references with corresponding values).
    param_val_ref = 2001 if ( output_val_ref < 2001 ) else output_val_ref
    for type, vars in fmi_parameters.items():
        for var in vars:
            scalar_variable_description = scalar_variable_node
            scalar_variable_description = addVariabilityAndCausalityToModelDescription( scalar_variable_description, fmi_version, type, False, True, verbose, modules )
            scalar_variable_description = scalar_variable_description.replace( '__VAR_TYPE__', type )
            scalar_variable_description = scalar_variable_description.replace( '__VAR_NAME__', var )
            scalar_variable_description = scalar_variable_description.replace( '__VAL_REF__', str( param_val_ref ) )
            if var in start_values:
                if isinstance( start_values[var], bool ): start_values[var] = int( start_values[var] )
                start_value_description = ' start=\"' + str( start_values[var] ) + '\"'
                scalar_variable_description = scalar_variable_description.replace( '__START_VALUE__', start_value_description )
                scalar_variable_description = scalar_variable_description.replace( '__INITIAL__', 'initial="exact"' )
                if ( True == verbose ): modules.log( '[DEBUG] Added start value to model description: ', var, '=', start_values[var] )
            else:
                scalar_variable_description = scalar_variable_description.replace( '__START_VALUE__', '' )
                scalar_variable_description = scalar_variable_description.replace( '__INITIAL__', '' )
            param_val_ref += 1
            # Write scalar variable description to file.
            model_description_scalars += scalar_variable_description;

    # Add backend class file and optional files.
    ( model_description_header, model_description_footer ) = \
        addOptionalFilesToModelDescription( model_description_header, model_description_footer, optional_files, fmi_version, verbose, modules)

    # Create new XML model description file.
    model_description_name = 'modelDescription.xml'
    model_description = open( model_description_name, 'w' )
    model_description.write( model_description_header );
    model_description.write( model_description_scalars );
    model_description.write( model_description_footer );
    model_description.close()

    return model_description_name


# Create script for running the backend implementation.
def createBackendScript( fmu_backend_class, fmu_backend_file, guid, verbose, modules ):
    # Extract file name from full path.
    file_name = modules.os.path.basename( fmu_backend_file )

    # Define name of script.
    backend_script_name = 'run_backend_{}.py'.format( guid )

    # Create script.
    backend_script = open( backend_script_name, 'w' )
    backend_script.write( 'import os.path\n')
    backend_script.write( 'from fmipp.export.runFMUBackend import runFMUBackend\n' )
    backend_script.write( 'backend_implementation = os.path.join( os.path.dirname( __file__ ), \'{backend_file}\' )\n'.format( backend_file = file_name ) )
    backend_script.write( 'runFMUBackend( backend_implementation, \'{backend_class}\' )\n'.format( backend_class = fmu_backend_class ) )

    if ( True == verbose ): modules.log( '[DEBUG] Created script for running the backend implementation: ', backend_script_name )

    return backend_script_name


# Get templates for the XML model description depending on the FMI version.
def getModelDescriptionTemplates( fmi_version, verbose, modules ):
    if ( '1' == fmi_version ): # FMI 1.0
        return fmi1GetModelDescriptionTemplates( verbose, modules )
    elif ( '2' == fmi_version ): # FMI 2.0
        return fmi2GetModelDescriptionTemplates( verbose, modules )


# Add variability to scalar variability description.
def addVariabilityAndCausalityToModelDescription( scalar_variable_description, fmi_version, type, is_input, is_parameter, verbose, modules ):
    if ( '1' == fmi_version ): # FMI 1.0
        return fmi1addVariabilityAndCausalityToModelDescription( scalar_variable_description, type, is_input, is_parameter, verbose, modules )
    elif ( '2' == fmi_version ): # FMI 2.0
        return fmi2addVariabilityAndCausalityToModelDescription( scalar_variable_description, type, is_input, is_parameter, verbose, modules )


# Add deck file as entry point to XML model description.
def addBackendClassFileToModelDescription( fmu_backend_class, fmu_backend_file, header, footer, fmi_version, verbose, modules ):
    if ( '1' == fmi_version ): # FMI 1.0
        return fmi1AddBackendClassFileToModelDescription( fmu_backend_class, fmu_backend_file, header, footer, verbose, modules )
    elif ( '2' == fmi_version ): # FMI 2.0
        return fmi2AddBackendClassFileToModelDescription( fmu_backend_class, fmu_backend_file, header, footer, verbose, modules )


# Add optional files to XML model description.
def addOptionalFilesToModelDescription( header, footer, optional_files, fmi_version, verbose, modules ):
    if ( '1' == fmi_version ):
        return fmi1AddOptionalFilesToModelDescription( optional_files, header, footer, verbose, modules )
    if ( '2' == fmi_version ):
        return fmi2AddOptionalFilesToModelDescription( optional_files, header, footer, verbose, modules )


# Create DLL for FMU.
def createSharedLibrary( fmi_model_identifier, fmi_version, verbose, modules ):
    if ( '1' == fmi_version ):
        return fmi1CreateSharedLibrary( fmi_model_identifier, verbose, modules )
    if ( '2' == fmi_version ):
        return fmi2CreateSharedLibrary( fmi_model_identifier, verbose, modules )
