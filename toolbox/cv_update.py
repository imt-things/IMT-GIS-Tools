import arcpy
from pathlib import Path

__version__ = "2022-09-12"


class CVUpdate:
    def __init__(self):
        # Define the tool (tool name is the name of the class).
        self.label = "Update Contingent Values"
        self.description = "Update Contingent Values"
        self.canRunInBackground = False
        # Use your own category here, or an existing one.
        self.category = "Data Management"
        # self.stylesheet = '' # I don't know how to use this yet.

    def getParameterInfo(self):
        # Define parameter definitions.
        # Refer to https://pro.arcgis.com/en/pro-app/latest/arcpy/geoprocessing_and_python/defining-parameters-in-a-python-toolbox.htm
        # and https://pro.arcgis.com/en/pro-app/latest/arcpy/geoprocessing_and_python/defining-parameter-data-types-in-a-python-toolbox.htm

        table = arcpy.Parameter(
            name="Contingent Value Table",
            displayName="Table",
            datatype="DETable",
            parameterType="Required",
            direction="Input",
        )

        gdb = arcpy.Parameter(
            name="GDB to update",
            displayName="Geodatabase to update",
            datatype="DEWorkspace",
            parameterType="Required",
            direction="Input",
        )

        return [table, gdb]

    def execute(self, parameters, messages):
        # The source code of your tool.
        # Get the parameters from our parameters list, then call a generic python function.
        # This separates the code doing the work from all the crazy code required to talk to ArcGIS.

        messages.addMessage(f"Running {self.label} version {__version__}")

        for param in parameters:
            messages.addMessage(f"Parameter: {param.name} = {param.valueAsText}")

        # prepare variables for different ways tools require the arguments passed
        gdb = parameters[1].valueAsText
        cv_table = parameters[0].valueAsText
        
        # currently for AGP
        fields = ["geom_type", "feat_group", "feat_category", "is_active", "keywords"]
        with arcpy.da.SearchCursor(cv_table, fields, where_clause="is_active=1") as cursor:
            values = [row for row in cursor]

        # get our values to append. use sets to drop duplicate values.
        groups = set([val[1] for val in values])
        point_vals = set([val for val in values if val[0] == "point"])
        poly_vals = set([val for val in values if val[0] == "polygon"])
        line_vals = set([val for val in values if val[0] == "line"])

        # append domain values and update CVs
        # TODO: Check for existing domains and decide how to handle them
        # TODO: retire CVs that exist in the gdb but not active in the CV table
        # TODO: make sure Other/Other is added to each CV (will have to be removed from list of CVs to retire)
        for i in groups:
            arcpy.AddCodedValueToDomain_management(gdb, "FeatureGroup", i, i)
        for i in line_vals:
            arcpy.AddCodedValueToDomain_management(gdb, "FeatureCategory(Line)", i[2], i[2])
            insert = f"feature_group CODED_VALUE '{i[1]}'; feature_category CODED_VALUE '{i[2]}'"
            arcpy.AddContingentValue_management(str(Path(gdb).joinpath("Event_Line")), "FeatureType", insert, )

        for i in point_vals:
            arcpy.AddCodedValueToDomain_management(gdb, "FeatureCategory(Point)", i[2], i[2])
            insert = f"feature_group CODED_VALUE '{i[1]}'; feature_category CODED_VALUE '{i[2]}'"
            arcpy.AddContingentValue_management(str(Path(gdb).joinpath("Event_Point")), "FeatureType", insert, )

        for i in poly_vals:
            arcpy.AddCodedValueToDomain_management(gdb, "FeatureCategory(Polygon)", i[2], i[2])
            insert = f"feature_group CODED_VALUE '{i[1]}'; feature_category CODED_VALUE '{i[2]}'"
            arcpy.AddContingentValue_management(str(Path(gdb).joinpath("Event_Polygon")), "FeatureType", insert, )

        # TODO: implement for AGOL

        # TODO:
        # 1. filter rows by is_active == 'Yes' ✅
        # 2. get unique values in feat_group column in each geom_type ✅
        # 3. update feature_group with unique group values (this will apply across all geometry types) ✅
        # 4. for each geom type, update geom feature_category domains ✅
        # 5. update CV's to match values
        # 6. retire CV's in GDB but not in table (or is_active = 0)

        # Todo: Add try/catch to catch cancellations and errors when cleanup is required.

        return
