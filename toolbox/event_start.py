import arcpy
from pathlib import Path
from datetime import date

__version__ = '2022-06-26'


class EventStart:
    def __init__(self):
        # Define the tool (tool name is the name of the class).
        self.label = 'Event Start'
        self.description = 'Start new incident'
        self.canRunInBackground = False
        # Use your own category here, or an existing one.
        self.category = 'Event'
        # self.stylesheet = '' # I don't know how to use this yet.

    def getParameterInfo(self):
        # Define parameter definitions.
        # Refer to https://pro.arcgis.com/en/pro-app/latest/arcpy/geoprocessing_and_python/defining-parameters-in-a-python-toolbox.htm

        inc_gdb = arcpy.Parameter(
            name='Incident Geodatabase',
            displayName='Incident Geodatabase',
            datatype='Workspace',
            parameterType='Required',
            direction='Input'
        )

        inc_name = arcpy.Parameter(
            name='Incident Name',
            displayName='Incident Name',
            datatype='GPString',
            parameterType='Required',
            direction='Input'
        )

        inc_commander = arcpy.Parameter(
            name='Incident Commander',
            displayName='Incident Commander',
            datatype='GPString',
            parameterType='Optional',
            direction='Input'
        )

        inc_num = arcpy.Parameter(
            name='Incident Number',
            displayName='Incident Number',
            datatype='GPString',
            parameterType='Optional',
            direction='Input'
        )

        return [inc_name, inc_commander, inc_num, inc_gdb]

    def execute(self, parameters, messages):
        # The source code of your tool.
        # Get the parameters from our parameters list, then call a generic python function.
        # This separates the code doing the work from all the crazy code required to talk to ArcGIS.

        messages.AddMessage(f'Running {self.label} version {__version__}')

        for param in parameters:
            messages.addMessage(
                f'Parameter: {param.name} = {param.valueAsText}')

        inc_name = arcpy.GetParameter(0)
        inc_commander = arcpy.GetParameter(1)
        inc_num = arcpy.GetParameter(2)
        inc_gdb = arcpy.GetParameter(3)

        # Ensure we don't have data in the table...that would indicate we are not creating an incident
        arcpy.env.workspace = inc_gdb
        assert arcpy.GetCount_management("DynamicText") == 0, messages.addMessage(
            "!!!Exiting -- Dynamic text table already contains data. Perhaps you want to join an incident, not create a new one?")

        messages.addMessage('Adding data to dynamic text table')

        data = {
            'inc_name': inc_name,
            'inc_num': inc_num,
            'inc_commander': inc_commander,
            }

        update_dyn_text(messages, inc_gdb, data)

        # Todo: Add try/catch to catch cancellations and errors when cleanup is required.

        return


def update_dyn_text(messages, inc_gdb, data):

    layer = f'{inc_gdb}/"DynamicText"'
    fields = data.keys()

    cursor = arcpy.da.InsertCursor(layer, fields)

    cursor.insertRow(data.values())

    del cursor

    return
