import arcpy
from pathlib import Path
from datetime import datetime

__version__ = '2022-04-25'


class ExportLayouts:
    def __init__(self) -> None:
        self.label = 'Export Project Layouts'
        self.description = 'Export selected layouts in project'
        self.canRunInBackground = True
        self.category = 'Products' # Use your own category here, or an existing one.
        #self.stylesheet = '' # I don't know how to use this yet.
    

    def getParameterInfo(self):
        # Define parameter definitions.
        # Refer to https://pro.arcgis.com/en/pro-app/latest/arcpy/geoprocessing_and_python/defining-parameters-in-a-python-toolbox.htm

        out_path = arcpy.Parameter(
            name='Output Directory',
            displayName='Output Directory',
            datatype='DEFolder',
            parameterType='Required',
            direction='Input'
        )

        layouts = arcpy.Parameter(
            name='Layouts',
            displayName='Layouts',
            parameterType='Required',
            datatype='String',
            direction='Input',
            multiValue=True
        )
    
        layouts.filter.type = "ValueList"
        layouts.filter.list = [layout.name for layout in arcpy.mp.ArcGISProject("CURRENT").listLayouts()]

        return [out_path, layouts]


    def execute(self, parameters, messages):
        messages.AddMessage(f'Running {self.label} version {__version__}')

        for param in parameters:
            messages.addMessage(f'Parameter: {param.name} = {param.valueAsText}')

        out_path = Path(parameters[0].valueAsText).resolve()

        layouts = parameters[1].valueAsText.split(';')
        layouts = [layout.replace("'", '') for layout in layouts]  # remove single quotes from layout parameter items

        export_layouts(messages, out_path, layouts)

        # Todo: Add try/catch to catch cancellations and errors when cleanup is required.

        return


def export_layouts(messages, out_path, layouts):
    messages.addMessage(f'Exporting layouts to {out_path}')
    aprx = arcpy.mp.ArcGISProject("CURRENT")

    layout_list = [aprx.listLayouts(layout)[0] for layout in layouts]

    for layout in layout_list:
        messages.addMessage(f'Exporting {layout.name}')

        # Change the formatting below to match your naming convention.
        out_format = f'{layout.name.lower()}_{int(layout.pageWidth)}x{int(layout.pageHeight)}_{layout.pageUnits}_{datetime.today().strftime("%Y%m%d")}_{datetime.now().strftime("%H%M")}'.replace(' ', '_').replace('-',"_").replace('.', '_')
        
        layout.exportToPDF(out_path.joinpath(out_format).with_suffix('.pdf'))
    return