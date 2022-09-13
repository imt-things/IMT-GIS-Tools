import pytest
import arcpy
from toolbox.cv_update import CVUpdate


fields = ["geom_type", "feat_group", "feat_category", "is_active", "keywords"]

data = [
    ("polygon", "Haz-Mat", "Hot-Zone", 1, ""),
    ("polygon", "Haz-Mat", "Cold-Zone", 1, ""),
    ("polygon", "Haz-Mat", "Warm-Zone", 1, ""),
    ("point", "Haz-Mat", "CCP", 1, ""),
    ("point", "Haz-Mat", "Decon", 1, ""),
    ("point", "ICS", "ICP", 1, ""),
    ("point", "Resources", "Engine", 1, ""),
    ("line", "Infrastructure", "Road Closure", 1, ""),
    ("line", "Resources", "Handline", 1, ""),
    ("point", "Resources", "Engine", 1, ""),  # duplicate to test catching of dup values
    ("point", "Haz-Mat", "Not Active", 0, "")  # not active
]

table_name = "Contingent_Values"


class TestCVUpdate:
    def test_cv_update(self, tmp_path, messages):
        gdb_path = tmp_path.joinpath("test.gdb")
        cv_table = f"{str(gdb_path.joinpath(table_name))}"

        # TODO: make this a fixture
        gdb = arcpy.CreateFileGDB_management(str(tmp_path), "test.gdb")
        gdb = arcpy.ImportXMLWorkspaceDocument_management(
            gdb, "event_gdb/event_gdb_schema.xml"
        )

        table = str(gdb_path.joinpath(table_name))
        with arcpy.da.InsertCursor(table, fields) as cursor:
            [cursor.insertRow(row) for row in data]

        # actual test
        cv_update = CVUpdate()
        params = cv_update.getParameterInfo()
        params[0].value = cv_table
        params[1].value = str(gdb_path)

        cv_update.execute(params, messages)

        domains = arcpy.da.ListDomains(gdb_path)

        domain_group_vals = [
            d.codedValues for d in domains if d.name == "FeatureGroup"
        ][0]

        domain_point_vals = [
            d.codedValues for d in domains if d.name == "FeatureCategory(Point)"
        ][0]

        domain_poly_vals = [
            d.codedValues for d in domains if d.name == "FeatureCategory(Polygon)"
        ][0]

        domain_line_vals = [
            d.codedValues for d in domains if d.name == "FeatureCategory(Line)"
        ][0]

        cv_point = arcpy.da.ListContingentValues(str(gdb_path.joinpath("Event_Point")))
        cv_poly = arcpy.da.ListContingentValues(str(gdb_path.joinpath("Event_Polygon")))
        cv_line = arcpy.da.ListContingentValues(str(gdb_path.joinpath("Event_Line")))

        assert len(domain_group_vals) == 5  # This appends so the default "Other/Unknown" is still there.
        assert len(domain_point_vals) == 5
        assert len(domain_poly_vals) == 4
        assert len(domain_line_vals) == 3
        assert len(cv_point) == 5
        assert len(cv_poly) == 4
        assert len(cv_line) == 3


