"""
Handle view logic for the Image Modal XBlock
"""
from __future__ import absolute_import
from six import text_type
from xblock.core import XBlock
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

    @XBlock.supports('multi_device')
    def student_view(self, context=None):
        """
        Build the fragment for the default student view
        """
        context = context or {}
        context.update({
            'display_name': self.display_name,
            'image_url': self.image_url,
            'thumbnail_url': self.thumbnail_url or self.image_url,
            'description': self.description,
            'xblock_id': text_type(self.scope_ids.usage_id),
            'alt_text': self.alt_text or self.display_name,
        })
        fragment = self.build_fragment(
            template='view.html',
            context=context,
            css=[
                'view.less.css',
                URL_FONT_AWESOME_CSS,
            ],
            js=[
                'draggabilly.pkgd.js',
                'view.js',
            ],
            js_init='ImageModalView',
        )
        return fragment
