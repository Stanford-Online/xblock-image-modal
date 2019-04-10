#!/usr/bin/env python
"""
Test XBlock workbench integration
"""
import unittest

from imagemodal import ImageModal


class TestWorkbench(unittest.TestCase):
    """
    Test XBlock workbench integration
    """

    def setUp(self):
        self.scenarios = ImageModal.workbench_scenarios()

    def _is_in_any_scenario(self, text):
        """
        Check if the text exists in any scenario
        """
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
