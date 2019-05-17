"""
Handle view logic for the XBlock
"""
from __future__ import absolute_import
from six import text_type
from xblockutils.resources import ResourceLoader
from xblockutils.studio_editable import StudioEditableXBlockMixin

from .mixins.fragment import XBlockFragmentBuilderMixin


URL_FONT_AWESOME_CSS = '//netdna.bootstrapcdn.com/font-awesome/3.2.1/css/font-awesome.css'  # nopep8


class ImageModalViewMixin(
        XBlockFragmentBuilderMixin,
        StudioEditableXBlockMixin,
):
    """
    Handle view logic for Image Modal XBlock instances
    """

    loader = ResourceLoader(__name__)
    static_css = [
        URL_FONT_AWESOME_CSS,
        'view.css',
    ]
    static_js = [
        'draggabilly.pkgd.min.js',
        'view.js',
    ]
    static_js_init = 'ImageModalView'

    def provide_context(self, context=None):
        """
        Build a context dictionary to render the student view
        """
        context = context or {}
        context = dict(context)
        context.update({
            'display_name': self.display_name,
            'image_url': self.image_url,
            'thumbnail_url': self.thumbnail_url or self.image_url,
            'description': self.description,
            'xblock_id': text_type(self.scope_ids.usage_id),
            'alt_text': self.alt_text or self.display_name,
        })
        return context
