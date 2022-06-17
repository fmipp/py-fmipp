# -----------------------------------------------------------------
# Copyright (c) 2022, AIT Austrian Institute of Technology GmbH.
# All rights reserved. See file FMIPP_LICENSE.txt for details.
# -----------------------------------------------------------------

#
# Collection of helper functions for creating FMU CS according to FMI 2.0
#

# Get templates for the XML model description depending on the FMI version.
def fmi2GetModelDescriptionTemplates( verbose, modules ):
    # Template string for XML model description header.
    header = '<?xml version="1.0" encoding="UTF-8"?>\n<fmiModelDescription\n\txmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"\n\tfmiVersion="2.0"\n\tmodelName="__MODEL_NAME__"\n\tguid="{__GUID__}"\n\tgenerationTool="FMI++ TRNSYS Export Utility"\n\tauthor="__USER__"\n\tgenerationDateAndTime="__DATE_AND_TIME__"\n\tvariableNamingConvention="flat"\n\tnumberOfEventIndicators="0">\n\t<CoSimulation\n\t\tmodelIdentifier="__MODEL_IDENTIFIER__"\n\t\tneedsExecutionTool="true"\n\t\tcanHandleVariableCommunicationStepSize="true"\n\t\tcanNotUseMemoryManagementFunctions="true"\n\t\tcanInterpolateInputs="false"\n\t\tmaxOutputDerivativeOrder="0"\n\t\tcanGetAndSetFMUstate="false"\n\t\tprovidesDirectionalDerivative="false"/>\n\t<VendorAnnotations>\n\t\t<Tool name="FMI++Export">\n\t\t\t<Executable\n\t\t\t\texecutableURI="__PYTHON_URI__"\n\t\t\t\tentryPointURI="fmu://resources/"\n\t\t\t\targuments="run_backend___GUID__.py"\n\t\t\t\tpreArguments=""\n\t\t\t\tpostArguments=""/>__ADDITIONAL_FILES__</Tool>\n\t</VendorAnnotations>\n\t<ModelVariables>\n'

    # Template string for XML model description of scalar variables.
    scalar_variable_node = '\t\t<ScalarVariable name="__VAR_NAME__" valueReference="__VAL_REF__" variability="__VARIABILITY__" causality="__CAUSALITY__" __INITIAL__>\n\t\t\t<__VAR_TYPE____START_VALUE__/>\n\t\t</ScalarVariable>\n'

    # Template string for XML model description footer.
    footer = '\t</ModelVariables>\n\t<ModelStructure/>\n</fmiModelDescription>'

    return ( header, scalar_variable_node, footer )


def fmi2addVariabilityAndCausalityToModelDescription( scalar_variable_description, type, is_input, is_parameter, verbose, modules ):
    if ( True is is_parameter ):
        scalar_variable_description = scalar_variable_description.replace( '__CAUSALITY__', 'parameter' )
        scalar_variable_description = scalar_variable_description.replace( '__VARIABILITY__', 'tunable' )
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
def fmi2AddOptionalFilesToModelDescription( optional_files, header, footer, verbose, modules ):
    if ( 0 == len( optional_files ) ):
        header = header.replace( '__ADDITIONAL_FILES__', '' )
    else:
        additional_files_description = ''
        indent = '\n\t\t'

        for file_name in optional_files:
            additional_files_description += indent + '\t<File file=\"fmu://resources/' + modules.os.path.basename( file_name ) + '\"/>'
            if ( True == verbose ): modules.log( '[DEBUG] Added additional file to model description: ', modules.os.path.basename( file_name ) )
        additional_files_description += indent

        header = header.replace( '__ADDITIONAL_FILES__', additional_files_description )

    return ( header, footer )


# Create shared library for FMU.
def fmi2CreateSharedLibrary( fmi_model_identifier, verbose, modules ):
    # Check platform to determine shared library file extension.
    system = modules.platform.system()
    if system =='Linux':
      file_ending = '.so'
    elif system == 'Windows':
      file_ending = '.dll'
    else: # system == 'Darwin'
      file_ending = '.dylib'

    # Define name of shared library based on platform.
    fmu_shared_library_name = fmi_model_identifier + file_ending

    for file in modules.os.listdir(modules.os.path.join(modules.os.path.dirname(__file__), 'bin')):
      if ((file.startswith('libfmi2.') or file.startswith('fmi2.')) and file.endswith(file_ending)):
        fmi2_dll_path = modules.os.path.join( modules.os.path.dirname( __file__ ), 'bin', file)

    if ( False == modules.os.path.isfile( fmi2_dll_path ) ):
        raise RuntimeError( '\n[ERROR] DLL not found: {}'.format( fmi2_dll_path ) )
    modules.shutil.copy( fmi2_dll_path, fmu_shared_library_name )

    if ( False == modules.os.path.isfile( fmu_shared_library_name ) ):
        raise RuntimeError( '\n[ERROR] Not able to create shared library: {}'.format( fmu_shared_library_name ) )

    return fmu_shared_library_name
