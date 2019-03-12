from xblock.core import XBlock
from xblockutils.resources import ResourceLoader


URL_FONT_AWESOME_CSS = '/'.join([
    '//netdna.bootstrapcdn.com'
    'font-awesome/3.2.1/css'
    'font-awesome.css'
])


class ImageModalView(object):

    _loader = ResourceLoader(__name__)

    # pylint: disable=no-member
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
            'xblock_id': unicode(self.scope_ids.usage_id),
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
    # pylint: enable=no-member
