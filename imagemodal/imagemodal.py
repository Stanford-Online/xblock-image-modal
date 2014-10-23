"""
This is the core logic for the Image Modal XBlock
"""
import os

import pkg_resources

from xblock.core import XBlock
from xblock.fields import Scope
from xblock.fields import String
from xblock.fragment import Fragment

DEFAULT_FIELDS = [
    'parent',
    'tags',
]


class ImageModal(XBlock):
    """
    A fullscreen image modal XBlock.
    """

    @staticmethod
    def workbench_scenarios():
        """
        Gather scenarios to be displayed in the workbench
        """
        return [
            ('Image Modal XBlock',
             """<sequence_demo>
                    <imagemodal />
                    <imagemodal
                        display_name="Image Modal With Thumbnail"
                        thumbnail_url="http://upload.wikimedia.org/wikipedia/commons/thumb/4/48/1853_Kaei_6_Japanese_Map_of_the_World_-_Geographicus_-_ChikyuBankokuHozu-nakajima-1853.jpg/640px-1853_Kaei_6_Japanese_Map_of_the_World_-_Geographicus_-_ChikyuBankokuHozu-nakajima-1853.jpg"
                    />
                </sequence_demo>
             """),
        ]

    display_name = String(
        default='Image Modal XBlock',
        scope=Scope.settings,
        help="This is the XBlock's display name",
    )

    image_url = String(
        default='http://upload.wikimedia.org/wikipedia/commons/4/48/1853_Kaei_6_Japanese_Map_of_the_World_-_Geographicus_-_ChikyuBankokuHozu-nakajima-1853.jpg',
        scope=Scope.settings,
        help='This is the location of the full-screen image to be displayed.',
    )

    thumbnail_url = String(
        default='',
        scope=Scope.settings,
        help='This is the (optional) location of a thumbnail image to be displayed before the main image has been enlarged.',
    )

    def student_view(self, context=None):
        """
        Build the fragment for the default student view
        """
        fragment = self.build_fragment(
            path_html='view.html',
            paths_css=[
                'view.less.min.css',
            ],
            paths_js=[
                'draggabilly.js.min.js',
                'view.js.min.js',
            ],
            urls_css=[
                '//netdna.bootstrapcdn.com/font-awesome/3.2.1/css/font-awesome.css',
            ],
            fragment_js='ImageModalView',
            context={
                'display_name': self.display_name,
                'image_url': self.image_url,
                'thumbnail_url': self.thumbnail_url or self.image_url,
            },
        )
        return fragment

    def studio_view(self, context=None):
        """
        Build the fragment for the edit/studio view

        Implementation is optional.
        """
        fragment = self.build_fragment(
            path_html='edit.html',
            paths_css=[
                'edit.less.min.css',
            ],
            paths_js=[
                'edit.js.min.js',
            ],
            fragment_js='ImageModalEdit',
        )
        return fragment

    @XBlock.json_handler
    def studio_view_save(self, data, suffix=''):
        """
        Save XBlock fields

        Returns: the new field values
        """

        self.display_name = data['display_name']
        self.image_url = data['image_url']
        self.thumbnail_url = data['thumbnail_url']
        return {
            'display_name': self.display_name,
            'image_url': self.image_url,
            'thumbnail_url': self.thumbnail_url,
        }

    def get_resource_string(self, path):
        """
        Retrieve string contents for the file path
        """
        path = os.path.join('public', path)
        resource_string = pkg_resources.resource_string(__name__, path)
        return resource_string.decode('utf8')

    def get_resource_url(self, path):
        """
        Retrieve a public URL for the file path
        """
        path = os.path.join('public', path)
        resource_url = self.runtime.local_resource_url(self, path)
        return resource_url

    def build_fragment(self,
        path_html='',
        paths_css=[],
        paths_js=[],
        urls_css=[],
        urls_js=[],
        fragment_js=None,
        context=None,
    ):
        """
        Assemble the HTML, JS, and CSS for an XBlock fragment
        """
        # If no context is provided, convert self.fields into a dict
        context = context or {
            key: getattr(self, key)
                for key in self.fields
                    if key not in DEFAULT_FIELDS
        }
        html_source = self.get_resource_string(path_html)
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
