"""
Mixin workbench behavior into XBlocks
"""


# pylint: disable=too-few-public-methods
class ImageModalScenarioMixin(object):
    """
    Provide a default test workbench for the XBlock
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
# pylint: enable=too-few-public-methods
