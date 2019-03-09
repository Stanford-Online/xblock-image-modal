"""
This is the core logic for the Image Modal XBlock
"""
from django.utils.translation import ugettext_lazy as _
from xblock.core import XBlock
from xblock.fields import Scope
from xblock.fields import String
from xblockutils.resources import ResourceLoader
from xblockutils.studio_editable import StudioEditableXBlockMixin

from .mixins.fragment import XBlockFragmentBuilderMixin

URL_FONT_AWESOME_CSS = '/'.join([
    '//netdna.bootstrapcdn.com'
    'font-awesome/3.2.1/css'
    'font-awesome.css'
])


# pylint: disable=too-many-ancestors
# pylint: disable=too-many-arguments
@XBlock.needs('i18n')
class ImageModal(
        XBlockFragmentBuilderMixin,
        StudioEditableXBlockMixin,
        XBlock,
):
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
            ('Image Modal XBlock, single',
             """<sequence_demo>
                    <imagemodal
                        display_name="Image Modal With Thumbnail"
                        thumbnail_url="http://upload.wikimedia.org/wikipedia/commons/thumb/4/48/1853_Kaei_6_Japanese_Map_of_the_World_-_Geographicus_-_ChikyuBankokuHozu-nakajima-1853.jpg/640px-1853_Kaei_6_Japanese_Map_of_the_World_-_Geographicus_-_ChikyuBankokuHozu-nakajima-1853.jpg"
                        description="Put screenreader text here"
                    />
                </sequence_demo>
             """),
            ('Image Modal XBlock, multiple',
             """<sequence_demo>
                    <vertical_demo>
                        <imagemodal
                            display_name="Image Modal With Thumbnail"
                            thumbnail_url="http://upload.wikimedia.org/wikipedia/commons/thumb/4/48/1853_Kaei_6_Japanese_Map_of_the_World_-_Geographicus_-_ChikyuBankokuHozu-nakajima-1853.jpg/640px-1853_Kaei_6_Japanese_Map_of_the_World_-_Geographicus_-_ChikyuBankokuHozu-nakajima-1853.jpg"
                            description="Put screenreader text here"
                        />
                        <imagemodal description="Write stuff here" />
                    </vertical_demo>
                    <vertical_demo>
                        <imagemodal description="Write stuff here" />
                        <imagemodal description="Write more here" />
                    </vertical_demo>
                </sequence_demo>
             """),
        ]
        # pylint: disable=line-too-long

    loader = ResourceLoader(__name__)

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
# pylint: enable=too-many-arguments
# pylint: enable=too-many-ancestors
