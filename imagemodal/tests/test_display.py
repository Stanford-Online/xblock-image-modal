#!/usr/bin/env python
# pylint: disable=missing-docstring,invalid-name,unused-import
import unittest

import django
from django.conf import settings
from mock import Mock
from opaque_keys.edx.locations import SlashSeparatedCourseKey
from xblock.field_data import DictFieldData

import imagemodal
from imagemodal import ImageModal


def make_an_xblock(**kwargs):
    """
    Helper method that creates a Free-text Response XBlock
    """
    course_id = SlashSeparatedCourseKey('foo', 'bar', 'baz')
    runtime = Mock(
        course_id=course_id,
        service=Mock(
            # Is there a cleaner mock to the `i18n` service?
            return_value=Mock(_catalog={}),
        ),
    )
    scope_ids = Mock()
    field_data = DictFieldData(kwargs)
    xblock = ImageModal(runtime, field_data, scope_ids)
    xblock.xmodule_runtime = runtime
    return xblock


class TestRender(unittest.TestCase):

    def setUp(self):
        try:
            settings.configure()
            django.setup()
        except RuntimeError:
            pass
        self.xblock = make_an_xblock()

    def test_render(self):
        student_view = self.xblock.student_view()
        html = student_view.content
        self.assertIsNotNone(html)
        self.assertNotEqual('', html)
        self.assertIn('imagemodal_block', html)


if __name__ == '__main__':
    unittest.main()
