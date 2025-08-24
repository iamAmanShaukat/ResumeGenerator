from typing import List, Dict, Any
from reportlab.platypus import Paragraph
from .base_builder import BaseBuilder

class ExperienceBuilder(BaseBuilder):
    @staticmethod
    def add_experience(content: List, experience: List[Dict[str, Any]], section_title: str, styles: Dict) -> None:
        """Add experience section."""
        if not experience:
            return

        content.append(Paragraph(section_title, styles['section_header']))
        content.append(BaseBuilder.create_section_divider())

        for exp in experience:
            # Job title
            title = exp.get('title', 'Position')
            content.append(Paragraph(title, styles['job_title']))

            # Company and duration
            company_info = []
            if exp.get('company'):
                company_info.append(f"<b>{exp['company']}</b>")
            if exp.get('location'):
                company_info.append(exp['location'])
            if exp.get('duration'):
                company_info.append(exp['duration'])

            if company_info:
                content.append(Paragraph(" | ".join(company_info), styles['company_info']))

            # Responsibilities
            responsibilities = exp.get('responsibilities', [])
            for resp in responsibilities:
                bullet_text = f"• {resp}"
                content.append(Paragraph(bullet_text, styles['bullet']))