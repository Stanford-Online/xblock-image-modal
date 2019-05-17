"""
This is the core logic for the XBlock
"""
from __future__ import absolute_import
from xblock.core import XBlock

from .mixins.scenario import XBlockWorkbenchMixin
from .models import ImageModalModelMixin
from .views import ImageModalViewMixin


@XBlock.needs('i18n')
class ImageModal(
        ImageModalModelMixin,
        ImageModalViewMixin,
        XBlockWorkbenchMixin,
        XBlock,
):
    """
    A fullscreen image modal XBlock.
    """
