import arcpy
from pathlib import Path
import csv

__version__ = '2022-03-14'

class UpdateDomains:
    def __init__(self):
        # Define the tool (tool name is the name of the class).
        self.label = 'Update Domains'
        self.description = 'Update Geodatabase Domains'
        self.canRunInBackground = True
        self.category = 'Data Management' # Use your own category here, or an existing one.
        #self.stylesheet = '' # I don't know how to use this yet.
    

    def getParameterInfo(self):
        # Define parameter definitions.
        # Refer to https://pro.arcgis.com/en/pro-app/latest/arcpy/geoprocessing_and_python/defining-parameters-in-a-python-toolbox.htm

        gdb = arcpy.Parameter(
            name='Geodatabase',
            displayName='Geodatabase to update domains on',
            datatype='DEWorkspace',
            parameterType='Required',
            direction='Input'
        )

        input_csv = arcpy.Parameter(
            name='Input Domains',
            displayName='CSV to add domains from',
            datatype='DEFile',
            parameterType='Required',
            direction='Input'
        )

        return [gdb, input_csv]

   
    def execute(self, parameters, messages):
        # The source code of your tool.
        # Get the parameters from our parameters list, then call a generic python function.
        # This separates the code doing the work from all the crazy code required to talk to ArcGIS.

        messages.AddMessage(f'Running {self.label} version {__version__}')

        for param in parameters:
            messages.addMessage(f'Parameter: {param.name} = {param.valueAsText}')

        gdb = parameters[0].valueAsText
        in_file = Path(parameters[1].valueAsText).resolve()
        
        add_domains(messages, gdb, in_file)
        
        

        # Todo: Add try/catch to catch cancellations and errors when cleanup is required.

        return

def add_domains(messages, gdb, in_file):
    # Todo: This should: read in file -> read in current domains -> delete ones no longer needed? -> add new domains -> update correct tables/fields

    values = []
    with in_file.open(newline='') as src:
        data = csv.DictReader(src)

        for row in data:
            row['domain_full'] = f'{row["domain_name"]}_{row["feat_type"]}'
            values.append(row)

    unique = set([value['domain_full'] for value in values])

    for dom in unique:

        # add value to FeatureGroup domain
        arcpy.AddCodedValueToDomain_management(gdb, 'FeatureGroup', dom, dom)
        messages.addMessage(f'Added {dom} to FeatureGroup domain')

        # create new domain
        # Todo: Add error checking....fails if the domain exists. If that's the case, we should update the coded values
        arcpy.CreateDomain_management(gdb, dom, field_type='TEXT', domain_type='CODED')
        messages.addMessage(f'Added domain: {dom}')

        # add coded values to new domain
        codes = {value['feature_name']: value['feature_name'] for value in values if value['domain_full'] == dom}
        for code in codes:
            short_code = code.replace(' ', '_')
            arcpy.AddCodedValueToDomain_management(gdb, dom, short_code, code)

        # # create subtype for domain



        # # add domain to field in subtype
        # if dom.contains('Polygons'):
        #     in_table = 'Event_Polygon'
        # elif dom.contains('Lines'):
        #     in_table = 'Event_Line'
        # elif dom.contains('Points'):
        #     in_table = 'Event_Point'
        # arcpy.AssignDomainToField_management(in_table, in_field, dom)


    return