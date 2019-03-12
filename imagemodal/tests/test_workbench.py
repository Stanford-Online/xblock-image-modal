#!/usr/bin/env python
"""
Test XBlock workbench integration
"""
import unittest

from mock import Mock
from opaque_keys.edx.locations import SlashSeparatedCourseKey
from xblock.field_data import DictFieldData

from imagemodal import ImageModal
from imagemodal.tests.test_display import make_an_xblock


class TestWorkbench(unittest.TestCase):
    """
    Test XBlock workbench integration
    """

    def setUp(self):
        self.scenarios = ImageModal.workbench_scenarios()

    def _is_in_any_scenario(self, text):
        contains = any([
            True
            for scenario in self.scenarios
            if text in scenario[1]
        ])
        return contains

    def test_load(self):
        self.assertGreater(len(self.scenarios), 0)

    def test_has_sequence(self):
        """
        Make sure at least one scenario contains a sequence
        """
        has_sequence = self._is_in_any_scenario('sequence_demo')
        self.assertTrue(has_sequence)

    def test_has_vertical(self):
        """
        Make sure at least one scenario contains a vertical
        """
        has_sequence = self._is_in_any_scenario('vertical_demo')
        self.assertTrue(has_sequence)


if __name__ == '__main__':
    unittest.main()
