"""
This is the core logic for the Image Modal XBlock
"""
import os

import pkg_resources

from django.utils.translation import ugettext_lazy as _

from xblock.core import XBlock
from xblock.fields import Scope
from xblock.fields import String
from xblock.fragment import Fragment

from xblockutils.studio_editable import StudioEditableXBlockMixin

DEFAULT_FIELDS = [
    'parent',
    'tags',
]


def get_resource_string(path):
    """
    Retrieve string contents for the file path
    """
    path = os.path.join('public', path)
    resource_string = pkg_resources.resource_string(__name__, path)
    return resource_string.decode('utf8')


# pylint: disable=too-many-ancestors
# pylint: disable=too-many-arguments
class ImageModal(StudioEditableXBlockMixin, XBlock):
    """
    A fullscreen image modal XBlock.
    """

    @staticmethod
    def workbench_scenarios():
        """
        Gather scenarios to be displayed in the workbench
        """
        # pylint: disable=no-self-use
        # pylint: disable=line-too-long
        return [
            ('Image Modal XBlock',
             """<sequence_demo>
                    <imagemodal />
                    <imagemodal
                        display_name="Image Modal With Thumbnail"
                        thumbnail_url="http://upload.wikimedia.org/wikipedia/commons/thumb/4/48/1853_Kaei_6_Japanese_Map_of_the_World_-_Geographicus_-_ChikyuBankokuHozu-nakajima-1853.jpg/640px-1853_Kaei_6_Japanese_Map_of_the_World_-_Geographicus_-_ChikyuBankokuHozu-nakajima-1853.jpg"
                        description="Put screenreader text here"
                    />
                </sequence_demo>
             """),
        ]
        # pylint: disable=line-too-long

    display_name = String(
        display_name=_('Display Name'),
        default='Image Modal XBlock',
        scope=Scope.settings,
        help=_("This is the XBlock's display name"),
    )

    image_url = String(
        display_name=_('Image URL'),
        default=(
            'http://upload.wikimedia.org/'
            'wikipedia/commons/4/48/'
            '1853_Kaei_6_Japanese_Map_of_the_World_-_'
            'Geographicus_-_ChikyuBankokuHozu-nakajima-1853.jpg'
        ),
        scope=Scope.settings,
        help=_(
            'This is the location of the full-screen image to be displayed.'
        ),
    )

    thumbnail_url = String(
        display_name=_('Thumbnail URL'),
        default='',
        scope=Scope.settings,
        help=_(
            'This is the (optional) location of a thumbnail image to be '
            'displayed before the main image has been enlarged.'
        ),
    )

    description = String(
        display_name=_('Description'),
        default='',
        scope=Scope.settings,
        help=_('Description text, displayed to screen readers'),
        multiline_editor=True,
    )

    alt_text = String(
        display_name=_('Alt Text'),
        default='',
        scope=Scope.settings,
        help=_(
            'This field allows you to add alternate or descriptive text'
            'that pertains to your image.'
        ),
    )

    editable_fields = [
        'display_name',
        'image_url',
        'thumbnail_url',
        'description',
        'alt_text',
    ]

    # pylint: disable=unused-argument
    # Decorate the view in order to support multiple devices e.g. mobile
    # See: https://openedx.atlassian.net/wiki/display/MA/Course+Blocks+API
    # section 'View @supports(multi_device) decorator'
    @XBlock.supports('multi_device')
    def student_view(self, context=None):
        """
        Build the fragment for the default student view
        """
        fragment = self.build_fragment(
            path_html='view.html',
            paths_css=[
                'view.less.css',
            ],
            paths_js=[
                'draggabilly.pkgd.js',
                'view.js',
            ],
            urls_css=[
                (
                    '//netdna.bootstrapcdn.com/'
                    'font-awesome/3.2.1/css/'
                    'font-awesome.css'
                ),
            ],
            fragment_js='ImageModalView',
            context={
                'display_name': self.display_name,
                'image_url': self.image_url,
                'thumbnail_url': self.thumbnail_url or self.image_url,
                'description': self.description,
                'xblock_id': unicode(self.scope_ids.usage_id),
                'alt_text': self.alt_text or self.display_name,
            },
        )
        return fragment
    # pylint: enable=unused-argument

    def get_resource_url(self, path):
        """
        Retrieve a public URL for the file path
        """
        path = os.path.join('public', path)
        resource_url = self.runtime.local_resource_url(self, path)
        return resource_url

    def build_fragment(
            self,
            path_html='',
            paths_css=None,
            paths_js=None,
            urls_css=None,
            urls_js=None,
            fragment_js=None,
            context=None,
    ):
        """
        Assemble the HTML, JS, and CSS for an XBlock fragment
        """
        paths_css = paths_css or []
        paths_js = paths_js or []
        urls_css = urls_css or []
        urls_js = urls_js or []
        # If no context is provided, convert self.fields into a dict
        context = context or {
            # pylint: disable=not-an-iterable
            key: getattr(self, key)
            for key in self.fields
            if key not in DEFAULT_FIELDS
        }
        html_source = get_resource_string(path_html)
        html_source = html_source.format(
            **context
        )
        fragment = Fragment(html_source)
        for path in paths_css:
            url = self.get_resource_url(path)
            fragment.add_css_url(url)
        for path in paths_js:
            url = self.get_resource_url(path)
            fragment.add_javascript_url(url)
        for url in urls_css:
            fragment.add_css_url(url)
        for url in urls_js:
            fragment.add_javascript_url(url)
        if fragment_js:
            fragment.initialize_js(fragment_js)
        return fragment
# pylint: enable=too-many-arguments
# pylint: enable=too-many-ancestors
