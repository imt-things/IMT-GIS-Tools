import pytest
import arcpy
from toolbox._template import _Template


class TestTemplate:

    def test_template(self, messages):
        # Get an instance of the tool.
        template = _Template()

        # Read default parameters.
        params = template.getParameterInfo()

        # Set some test values into the instance
        params[0].value = 2
        params[1].value = 5

        # Run it.
        assert template.execute(params, messages) == 7
        