import arcpy
from pathlib import Path
from datetime import datetime

__version__ = '2022-04-25'


class ExportLayouts:
    def __init__(self) -> None:
        self.label = 'Export Project Layouts'
        self.description = 'Export selected layouts in project'
        self.canRunInBackground = True
        # Use your own category here, or an existing one.
        self.category = 'Products'
        # self.stylesheet = '' # I don't know how to use this yet.

    def getParameterInfo(self, aprx_path="CURRENT"):
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
        layouts.filter.list = [
            layout.name for layout in arcpy.mp.ArcGISProject(aprx_path).listLayouts()]

        return [out_path, layouts]

    def execute(self, parameters, messages, aprx_path="CURRENT"):
        messages.addMessage(f'Running {self.label} version {__version__}')

        for param in parameters:
            messages.addMessage(
                f'Parameter: {param.name} = {param.valueAsText}')

        out_path = Path(parameters[0].valueAsText).resolve()

        layouts = parameters[1].valueAsText.split(';')
        # remove single quotes from layout parameter items
        layouts = [layout.replace("'", '') for layout in layouts]

        messages.addMessage(f'Exporting layouts to {out_path}')
        aprx = arcpy.mp.ArcGISProject(aprx_path)

        layout_list = [aprx.listLayouts(layout)[0] for layout in layouts]

        for layout in layout_list:
            messages.addMessage(f'Exporting {layout.name}')

            # TODO: Move this to an .env or similar...also make it more user friendly
            # Change the formatting below to match your naming convention.
            out_format = f'{layout.name.lower()}_{int(layout.pageWidth)}x{int(layout.pageHeight)}_{layout.pageUnits}_{datetime.today().strftime("%Y%m%d")}_{datetime.now().strftime("%H%M")}'
            out_filename = out_format.replace(' ', '_').replace('-', "_").replace('.', '_')

            layout.exportToPDF(out_path.joinpath(
                out_filename).with_suffix('.pdf'))

        return True
