from typing import List, Dict

from reportlab.platypus import Paragraph
from .base_builder import BaseBuilder

class AchievementsBuilder(BaseBuilder):
    @staticmethod
    def add_achievements(content: List, achievements: List[str], styles: Dict) -> None:
        """Add achievements section."""
        if not achievements:
            return

        content.append(Paragraph("Achievements", styles['section_header']))
        content.append(BaseBuilder.create_section_divider())

        for achievement in achievements:
            bullet_text = f"• {achievement}"
            content.append(Paragraph(bullet_text, styles['bullet']))