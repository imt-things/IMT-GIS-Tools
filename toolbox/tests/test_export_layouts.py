import pytest
from toolbox.export_layouts import ExportLayouts

class TestExportLayouts:

    def test_export_layouts_one(self, tmp_path, messages, test_aprx_path):
        """Tests that we get a single pdf output when a single layout is passed

        Args:
            tmp_path (_type_): _description_
            messages (_type_): _description_
            test_aprx_path (_type_): _description_
        """
        exp_layouts = ExportLayouts()
        params = exp_layouts.getParameterInfo(aprx_path=test_aprx_path)
        params[0].value = str(tmp_path)
        params[1].value = params[1].filter.list[0]
        exp_layouts.execute(params, messages, aprx_path=test_aprx_path)

        assert len(list(tmp_path.iterdir())) == 1


    def test_export_layouts_two(self, tmp_path, messages, test_aprx_path):
        """Tests that we get two (multiple) pdf outputs two (multiple) layouts are passed

        Args:
            tmp_path (_type_): _description_
            messages (_type_): _description_
            test_aprx_path (_type_): _description_
        """
        exp_layouts = ExportLayouts()
        params = exp_layouts.getParameterInfo(aprx_path=test_aprx_path)
        params[0].value = str(tmp_path)
        params[1].value = f"{params[1].filter.list[0]};{params[1].filter.list[1]}"
        exp_layouts.execute(params, messages, aprx_path=test_aprx_path)

        assert len(list(tmp_path.iterdir())) == 2
