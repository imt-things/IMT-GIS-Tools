__version__ = "2022-12-31"


class UpdateDomains:
    def __init__(self):
        # Define the tool (tool name is the name of the class).
        self.label = "Update Domains"
        self.description = "Update Geodatabase Domains"
        self.canRunInBackground = True
        self.category = (
            "Data Management"  # Use your own category here, or an existing one.
        )
        # self.stylesheet = '' # I don't know how to use this yet.

    def getParameterInfo(self):
        # Define parameter definitions.
        # Refer to https://pro.arcgis.com/en/pro-app/latest/arcpy/geoprocessing_and_python/defining-parameters-in-a-python-toolbox.htm

        gdb = arcpy.Parameter(
            name="Geodatabase",
            displayName="Geodatabase to update domains on",
            datatype="DEWorkspace",
            parameterType="Required",
            direction="Input",
        )

        input_table = arcpy.Parameter(  # TODO: this should be a table, not csv
            name="Input Domains",
            displayName="CSV to add domains from",
            datatype="DEFile",
            parameterType="Required",
            direction="Input",
        )

        return [gdb, input_table]

    def execute(self, parameters, messages):
        # The source code of your tool.
        # Get the parameters from our parameters list, then call a generic python function.
        # This separates the code doing the work from all the crazy code required to talk to ArcGIS.

        messages.AddMessage(f"Running {self.label} version {__version__}")

        for param in parameters:
            messages.addMessage(f"Parameter: {param.name} = {param.valueAsText}")

        gdb = parameters[0].valueAsText
        in_file = Path(parameters[1].valueAsText).resolve()

        update_domains(messages, gdb, in_file)

        # Todo: Add try/catch to catch cancellations and errors when cleanup is required.

        return


# Determine if the geodatabase is a file geodatabase or an ArcGIS Online geodatabase and build the domain pairs
def update_domains(messages, gdb, in_file):
    # [ ] read in table of domains -> table_doms
    # [ ] read in existing domains -> existing_doms
    # [x] find domains to update (retire)  -> set(existing_doms) - set(table_doms)
    # [x] find domains to add -> set(table_doms) - set(existing_doms)
    # [ ] build dict for operations
    # [ ] determine if we are using file_gdb or AGOL
    # [ ] perform appropriate operations
    # [ ] update contingent values from table

    # NOTES:
    # sets can't contain dicts...going to have to run a loop for each geometry type/feature category

    def _get_table_doms() -> set:
        doms: set = set([])
        return doms

    def _get_existing_doms() -> set:
        doms: set = set([])
        return doms

    def _update_file_gdb_doms(to_add: set, to_retire: set):
        return

    def _update_agol_doms(to_add: set, to_retire: set):
        # TODO: does this append/update or do it replace?
        for field in ["feature_category", "feature_group"]:

            update_dict = {
                "fields": [
                    {
                        "name": field,
                        "domain": {
                            "type": "codedValue",
                            "name": "FeatureCategory(Polygon)",  # TODO: shred this out to geometries
                            "codedValues": [
                                {"name": val, "code": val} for val in to_add
                            ],
                        },
                    }
                ]
            }
        return

    gdb_type = "AGOL"  # TODO: 'agol' or 'fileggdb'...how do we determine this?

    table_doms = _get_table_doms()  # TODO: implement this
    existing_doms = _get_existing_doms()  # TODO: implement this

    to_add = table_doms - existing_doms
    to_retire = existing_doms - table_doms

    if gdb_type == "AGOL":
        _update_agol_doms(to_add, to_retire)
    elif gdb_type == "fileggdb":
        _update_file_gdb_doms(to_add, to_retire)
    else:
        raise NotImplementedError

    return

    # TODO: test that domains get synced when working offline


# def update_domains_filegdb():
#     # Todo: This should: read in file -> read in current domains -> delete ones no longer needed? -> add new domains -> update correct tables/fields

#     values = []
#     with in_file.open(newline="") as src:
#         data = csv.DictReader(src)

#         for row in data:
#             row["domain_full"] = f'{row["domain_name"]}_{row["feat_type"]}'
#             values.append(row)

#     unique = set([value["domain_full"] for value in values])

#     for dom in unique:

#         # add value to FeatureGroup domain
#         arcpy.AddCodedValueToDomain_management(gdb, "FeatureGroup", dom, dom)
#         messages.addMessage(f"Added {dom} to FeatureGroup domain")

#         # create new domain
#         # Todo: Add error checking....fails if the domain exists. If that's the case, we should update the coded values
#         arcpy.CreateDomain_management(gdb, dom, field_type="TEXT", domain_type="CODED")
#         messages.addMessage(f"Added domain: {dom}")

#         # add coded values to new domain
#         codes = {
#             value["feature_name"]: value["feature_name"]
#             for value in values
#             if value["domain_full"] == dom
#         }
#         for code in codes:
#             short_code = code.replace(" ", "_")
#             arcpy.AddCodedValueToDomain_management(gdb, dom, short_code, code)

#     return


# def update_domain_agol():
#     # Todo: completely untested!!!

#     from arcgis import GIS, features

#     # connect to AGOL
#     gis = GIS(username="", password="")

#     # get the feature service
#     service = gis.content.get("", feature_service_id="")

#     # get the feature layer
#     layer = service.layers[0]
#     features = features.FeatureLayerCollection.fromitem(service)

#     # get current domains
#     properties = features.properties

#     # delete ones no longer needed?
#     pass

#     # add new domains
#     pass

#     # update correct tables/fields
#     result = layer.manager.update_definition(update_dict)

#     update_dict = {
#         "fields": [
#             {
#                 "name": "feature_category",
#                 "domain": {
#                     "type": "codedValue",
#                     "name": "FeatureCategory_Point",
#                     "codedValues": [
#                         {"name": "PyTest3", "code": "PyTest3"},
#                         {"name": "PyTest4", "code": "PyTest4"},
#                     ],
#                 },
#             }
#         ]
#     }


# result = layer.manager.update_definition(update_dict)
