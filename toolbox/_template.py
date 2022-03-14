import arcpy
from pathlib import Path
from datetime import date

__version__ = '2022-02-12'

class _Template:
    def __init__(self):
        # Define the tool (tool name is the name of the class).
        self.label = 'Tool Template'
        self.description = 'Just a template'
        self.canRunInBackground = True
        self.category = 'Debugging' # Use your own category here, or an existing one.
        #self.stylesheet = '' # I don't know how to use this yet.
    

    def getParameterInfo(self):
        # Define parameter definitions.
        # Refer to https://pro.arcgis.com/en/pro-app/latest/arcpy/geoprocessing_and_python/defining-parameters-in-a-python-toolbox.htm

        start_number = arcpy.Parameter(
            name='Start Number',
            displayName='Number to add to',
            datatype='GPLong',
            parameterType='Required',
            direction='Input'
        )

        add_number = arcpy.Parameter(
            name='Number to add',
            displayName='Number to add',
            datatype='GPLong',
            parameterType='Required',
            direction='Input'
        )

        add_number.value = 5  # Set default value

        return [start_number, add_number]

   
    def execute(self, parameters, messages):
        # The source code of your tool.
        # Get the parameters from our parameters list, then call a generic python function.
        # This separates the code doing the work from all the crazy code required to talk to ArcGIS.

        messages.AddMessage(f'Running {self.label} version {__version__}')

        for param in parameters:
            messages.addMessage(f'Parameter: {param.name} = {param.valueAsText}')

        base_num = arcpy.GetParameter(0)
        add_num = arcpy.GetParameter(1)

        messages.addMessage(f'{base_num+add_num}')
        
        add_nums(messages, base_num, add_num)
        
        

        # Todo: Add try/catch to catch cancellations and errors when cleanup is required.

        return

def add_nums(messages, x, y):
    messages.addMessage(x + y)
    return