import arcpy

__version__ = "2022-09-09"


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

        # currently for AGP
        # prepare variables for different ways tools require the arguments passed
        gdb = parameters[1].valueAsText
        cv_table = parameters[0].valueAsText

        fields = ["geom_type", "feat_group", "feat_category", "is_active", "keywords"]
        values = [row for row in arcpy.da.SearchCursor(cv_table, fields)] # TODO: filer is_active == "Yes"
        groups = set([val[1] for val in values])
        point_vals = set([val[2] for val in values if val[0] == "point"])
        poly_vals = set([val[2] for val in values if val[0] == "polygon"])
        line_vals = set([val[2] for val in values if val[0] == "line"])

        # TODO: Check for existing domains and decide how to handle them
        for i in groups:
            arcpy.AddCodedValueToDomain_management(gdb, "FeatureGroup", i, i)

        for i in point_vals:
            arcpy.AddCodedValueToDomain_management(gdb, "FeatureCategory(Point)", i, i)

        for i in poly_vals:
            arcpy.AddCodedValueToDomain_management(gdb, "FeatureCategory(Polygon)", i, i)

        for i in line_vals:
            arcpy.AddCodedValueToDomain_management(gdb, "FeatureCategory(Line)", i, i)

        # TODO: impliment for AGOL

        # TODO:
        # 1. filter rows by is_active == 'Yes'
        # 2. get unique values in feat_group column in each geom_type
        # 3. update feature_group with unique group values (this will apply across all geometry types)
        # 4. for each geom type, update geom feature_category domains
        # 5. update CV's to match values

        # Todo: Add try/catch to catch cancellations and errors when cleanup is required.

        return
