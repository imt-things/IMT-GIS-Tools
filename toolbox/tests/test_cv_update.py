import pytest
import arcpy
from toolbox.cv_update import CVUpdate


fields = ["geom_type", "feat_group", "feat_category", "is_active", "keywords"]

data = [
    ("polygon", "Haz-Mat", "Hot-Zone", "Yes", ""),
    ("polygon", "Haz-Mat", "Cold-Zone", "Yes", ""),
    ("polygon", "Haz-Mat", "Warm-Zone", "Yes", ""),
    ("point", "Haz-Mat", "CCP", "Yes", ""),
    ("point", "Haz-Mat", "Decon", "Yes", ""),
    ("point", "ICS", "ICP", "Yes", ""),
    ("point", "Response Resources", "Engine", "Yes", ""),
    ("line", "Infrastructure", "Road Closure", "Yes", ""),
    ("line", "Response Resources", "Handline", "Yes", ""),
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

        table = f"{str(gdb_path)}\{table_name}"
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
            d.codedValues
            for d in domains
            if d.name == "FeatureGroup"
        ][0]

        domain_point_vals = [
            d.codedValues
            for d in domains
            if d.name == "FeatureCategory(Point)"
        ][0]

        domain_poly_vals = [
            d.codedValues
            for d in domains
            if d.name == "FeatureCategory(Polygon)"
        ][0]

        domain_line_vals = [
            d.codedValues
            for d in domains
            if d.name == "FeatureCategory(Line)"
        ][0]

        assert len(domain_group_vals) == 5 # This appends so the default "Other/Unknown" is still there.
        assert len(domain_point_vals) == 4
        assert len(domain_poly_vals) == 3
        assert len(domain_line_vals) == 2
