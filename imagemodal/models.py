from django.utils.translation import ugettext_lazy as _
from xblock.fields import Scope
from xblock.fields import String


_default_fields = [
    'name',
    'parent',
    'tags',
]


class ImageModalModel(object):

    display_name = String(
        display_name=_('Display Name'),
        default='Image Modal XBlock',
        scope=Scope.settings,
    )
    """
    This is the XBlock's display name
    """

    image_url = String(
        display_name=_('Image URL'),
        default=(
            'http://upload.wikimedia.org/'
            'wikipedia/commons/4/48/'
            '1853_Kaei_6_Japanese_Map_of_the_World_-_'
            'Geographicus_-_ChikyuBankokuHozu-nakajima-1853.jpg'
        ),
        scope=Scope.settings,
    )
    """
    This is the location of the full-screen image to be displayed.
    """

    thumbnail_url = String(
        display_name=_('Thumbnail URL'),
        default='',
        scope=Scope.settings,
    )
    """
    This is the (optional) location of a thumbnail image to be
    displayed before the main image has been enlarged.
    """

    description = String(
        display_name=_('Description'),
        default='',
        scope=Scope.settings,
        multiline_editor=True,
    )
    """
    Description text, displayed to screen readers
    """


    def __init__(self, *args, **kwargs):
        """
        TODO: Move this to a mixin
        """
        super(ImageModalModel, self).__init__(*args, **kwargs)
        editable_fields = getattr(self, 'editable_fields', [])
        if len(editable_fields) == 0:
            self.editable_fields = [
                field
                for field in self.fields.keys()
                if field not in _default_fields
            ]
        self.alt_text = String(
            display_name=_('Alt Text'),
            default='',
            scope=Scope.settings,
        )
        """
        This field allows you to add alternate or descriptive text
        that pertains to your image.
        """
        print(self.alt_text.__doc__)
        self.alt_text.help=self.alt_text.__doc__
        return
        for field in self.editable_fields:
            attribute = self.fields[field]
            attribute.help = attribute.__doc__
            print(attribute.__doc__)
