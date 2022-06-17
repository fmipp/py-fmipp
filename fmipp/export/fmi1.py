# -----------------------------------------------------------------
# Copyright (c) 2022, AIT Austrian Institute of Technology GmbH.
# All rights reserved. See file FMIPP_LICENSE.txt for details.
# -----------------------------------------------------------------

#
# Collection of helper functions for creating FMU CS according to FMI 1.0
#
import platform

# Get templates for the XML model description depending on the FMI version.
def fmi1GetModelDescriptionTemplates( verbose, modules ):
    # Template string for XML model description header.
    header = '<?xml version="1.0" encoding="UTF-8"?>\n<fmiModelDescription fmiVersion="1.0" modelName="__MODEL_NAME__" modelIdentifier="__MODEL_IDENTIFIER__" description="TRNSYS FMI CS export" generationTool="FMI++ TRNSYS Export Utility" generationDateAndTime="__DATE_AND_TIME__" variableNamingConvention="flat" numberOfContinuousStates="0" numberOfEventIndicators="0" author="__USER__" guid="{__GUID__}">\n\t<VendorAnnotations>\n\t\t<Tool name="python">\n\t\t\t<Executable arguments="run_backend___GUID__.py" executableURI="__PYTHON_URI__"/>\n\t\t</Tool>\n\t</VendorAnnotations>\n\t<ModelVariables>\n'

    # Template string for XML model description of scalar variables.
    scalar_variable_node = '\t\t<ScalarVariable name="__VAR_NAME__" valueReference="__VAL_REF__" variability="__VARIABILITY__" causality="__CAUSALITY__">\n\t\t\t<__VAR_TYPE____START_VALUE__/>\n\t\t</ScalarVariable>\n'

    # Template string for XML model description footer.
    footer = '\t</ModelVariables>\n\t<Implementation>\n\t\t<CoSimulation_Tool>\n\t\t\t<Capabilities canHandleVariableCommunicationStepSize="true" canHandleEvents="true" canRejectSteps="false" canInterpolateInputs="false" maxOutputDerivativeOrder="0" canRunAsynchronuously="false" canBeInstantiatedOnlyOncePerProcess="false" canNotUseMemoryManagementFunctions="true"/>\n\t\t\t<Model entryPoint="fmu://resources/" manualStart="false" type="application/x-python">__ADDITIONAL_FILES__</Model>\n\t\t</CoSimulation_Tool>\n\t</Implementation>\n</fmiModelDescription>'

    return ( header, scalar_variable_node, footer )


def fmi1addVariabilityAndCausalityToModelDescription( scalar_variable_description, type, is_input, is_parameter, verbose, modules ):
    if ( True is is_parameter ):
        scalar_variable_description = scalar_variable_description.replace( '__CAUSALITY__', 'input' )
        scalar_variable_description = scalar_variable_description.replace( '__VARIABILITY__', 'parameter' )
    elif ( True is is_input and False is is_parameter ):
        scalar_variable_description = scalar_variable_description.replace( '__CAUSALITY__', 'input' )
        if ( 'Real' is type ):
            scalar_variable_description = scalar_variable_description.replace( '__VARIABILITY__', 'continuous' )
        else:
            scalar_variable_description = scalar_variable_description.replace( '__VARIABILITY__', 'discrete' )
    elif ( False is is_input and False is is_parameter ):
        scalar_variable_description = scalar_variable_description.replace( '__CAUSALITY__', 'output' )
        if ( 'Real' is type ):
            scalar_variable_description = scalar_variable_description.replace( '__VARIABILITY__', 'continuous' )
        else:
            scalar_variable_description = scalar_variable_description.replace( '__VARIABILITY__', 'discrete' )
    return scalar_variable_description


# Add optional files to XML model description.
def fmi1AddOptionalFilesToModelDescription( optional_files, header, footer, verbose, modules ):
    if ( 0 == len( optional_files ) ):
        footer = footer.replace( '__ADDITIONAL_FILES__', '' )
    else:
        additional_files_description = ''
        indent = '\n\t\t\t'

        for file_name in optional_files:
            additional_files_description += indent + '\t<File file=\"fmu://resources/' + modules.os.path.basename( file_name ) + '\"/>'
            if ( True == verbose ): modules.log( '[DEBUG] Added additional file to model description: ', modules.os.path.basename( file_name ) )
        additional_files_description += indent

        footer = footer.replace( '__ADDITIONAL_FILES__', additional_files_description )

    return ( header, footer )


# Create shared library for FMU.
def fmi1CreateSharedLibrary( fmi_model_identifier, verbose, modules ):
    # Define name and extension of shared library file based on platform.
    system = modules.platform.system()
    if system == 'Linux':
      fmu_shared_library_name = fmi_model_identifier + '.so'
    elif system == 'Windows':
      fmu_shared_library_name = fmi_model_identifier + '.dll'
    else: # system == 'Darwin'
      fmu_shared_library_name = fmi_model_identifier + '.dylib'

    # Check if batch file for build process exists.
    build_process_batch_file = modules.os.path.join( modules.os.path.dirname( __file__ ), 'scripts', 'fmi1_build.bat' )
    if ( False == modules.os.path.isfile( build_process_batch_file ) ):
        raise RuntimeError( '\n[ERROR] Could not find file: {}'.format( build_process_batch_file ) )
    # Remove possible leftovers from previous builds.
    for file_name in modules.glob.glob( fmi_model_identifier + '.*' ): modules.os.remove( file_name )
    if ( True == modules.os.path.isfile( 'fmiFunctions.obj' ) ): modules.os.remove( 'fmiFunctions.obj' )
    # Compile FMU shared library.
    build_process = modules.subprocess.Popen( [ build_process_batch_file, fmi_model_identifier ] )
    stdout, stderr = build_process.communicate()

    if ( False == modules.os.path.isfile( fmu_shared_library_name ) ):
        raise RuntimeError( '\n[ERROR] Not able to create shared library: {}'.format( fmu_shared_library_name ) )

    return fmu_shared_library_name
