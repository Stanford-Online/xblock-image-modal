"""
Mixin fragment/html behavior into XBlocks
"""
from django.template.context import Context
from xblock.fragment import Fragment


class XBlockFragmentBuilderMixin(object):
    """
    Create a default XBlock fragment builder
    """

    def build_fragment(
            self,
            template='',
            context=None,
            css=None,
            js=None,
            js_init=None,
    ):
        """
        Creates a fragment for display.
        """
        template = 'templates/' + template
        context = context or {}
        css = css or []
        js = js or []
        rendered_template = ''
        if template:
            rendered_template = self.loader.render_django_template(
                template,
                context=Context(context),
                i18n_service=self.runtime.service(self, 'i18n'),
            )
        fragment = Fragment(rendered_template)
        for item in css:
            if item.startswith('/'):
                url = item
            else:
                item = 'public/' + item
                url = self.runtime.local_resource_url(self, item)
            fragment.add_css_url(url)
        for item in js:
            item = 'public/' + item
            url = self.runtime.local_resource_url(self, item)
            fragment.add_javascript_url(url)
        if js_init:
            fragment.initialize_js(js_init)
        return fragment
