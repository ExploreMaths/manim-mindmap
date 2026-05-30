__all__ = [
    'LayoutFactory',
]
from .tidy_tree import TidyTreeLayout
from .time_line import TimeLineLayout
from .layout_config import LayoutType, LayoutConfig

class LayoutFactory:
    '''布局算法工厂'''
    @staticmethod
    def create_layout(
        layout_type: LayoutType,
        root,
        layout_config:LayoutConfig
    ):
        match layout_type:
            case LayoutType.MindMap:
                kwargs = layout_config.mindmap
                return TidyTreeLayout(root, **kwargs)
            case LayoutType.TimeLine:
                kwargs = layout_config.timeline
                return TimeLineLayout(root, **kwargs)