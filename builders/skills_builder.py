from typing import List, Dict, Any
from reportlab.platypus import Table, Paragraph

from utils.table import TableUtils
from .base_builder import BaseBuilder

class SkillsBuilder(BaseBuilder):
    @staticmethod
    def add_skills(content: List, technical_skills: Dict[str, Any], styles: Dict) -> None:
        """Add technical skills with dynamic column width calculation."""
        if not technical_skills:
            return

        content.append(Paragraph("Technical Skills", styles['section_header']))
        content.append(BaseBuilder.create_section_divider())

        # Prepare skills data
        skills_data = []
        for category, skills in technical_skills.items():
            cat_title = category.replace('_', ' ').title() + ":"
            if isinstance(skills, list):
                skills_text = ", ".join(skills)
            else:
                skills_text = str(skills)
            skills_data.append([cat_title, skills_text])

        if skills_data:
            # Create skills table
            skills_table = TableUtils.create_skills_table(skills_data)
            content.append(skills_table)