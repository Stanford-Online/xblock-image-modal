"""
This is the core logic for the Image Modal XBlock
"""
from xblock.core import XBlock
from xblockutils.studio_editable import StudioEditableXBlockMixin

from .mixins.fragment import XBlockFragmentBuilderMixin
from .mixins.scenario import XBlockWorkbenchMixin
from .models import ImageModalModel
from .views import ImageModalView


@XBlock.needs('i18n')
class ImageModal(
        ImageModalModel,
        ImageModalView,
        XBlockWorkbenchMixin,
        XBlockFragmentBuilderMixin,
        StudioEditableXBlockMixin,
        XBlock,
):
    """
    A fullscreen image modal XBlock.
    """
    pass
