"""
Handle data access logic for the XBlock
"""
from __future__ import absolute_import
from django.utils.translation import ugettext_lazy as _
from xblock.fields import Scope
from xblock.fields import String


class ImageModalModelMixin(object):
    """
    Handle data access for Image Modal XBlock instances
    """

    editable_fields = [
        'display_name',
        'image_url',
        'thumbnail_url',
        'description',
        'alt_text',
    ]

    show_in_read_only_mode = True

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
