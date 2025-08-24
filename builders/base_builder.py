from reportlab.platypus import HRFlowable
from styles.constants import Colors


class BaseBuilder:
    @staticmethod
    def create_section_divider() -> HRFlowable:
        """Create a professional section divider."""
        return HRFlowable(
            width="100%",
            thickness=1,
            lineCap='round',
            color=Colors.PRIMARY,
            spaceBefore=5,
            spaceAfter=5
        )