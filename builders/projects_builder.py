from typing import List, Dict, Any
from reportlab.platypus import Paragraph
from .base_builder import BaseBuilder

class ProjectsBuilder(BaseBuilder):
    @staticmethod
    def add_projects(content: List, projects: List[Dict[str, Any]], styles: Dict) -> None:
        """Add projects section with enhanced formatting."""
        if not projects:
            return

        content.append(Paragraph("Projects", styles['section_header']))
        content.append(BaseBuilder.create_section_divider())

        for proj in projects:
            # Project name and source
            proj_name = proj.get('name', 'Project')
            proj_source = proj.get('source', '')

            if proj_source:
                if proj_source.startswith('http'):
                    proj_header = f"<b><link href='{proj_source}'>{proj_name}</link></b>"
                else:
                    proj_header = f"<b>{proj_name}</b> ({proj_source})"
            else:
                proj_header = f"<b>{proj_name}</b>"

            content.append(Paragraph(proj_header, styles['job_title']))

            # Technologies used
            if proj.get('technologies'):
                tech_text = f"<i>Technologies: {', '.join(proj['technologies'])}</i>"
                content.append(Paragraph(tech_text, styles['company_info']))

            # Project description
            description = proj.get('description', [])
            if isinstance(description, str):
                description = [description]

            for desc in description:
                bullet_text = f"• {desc}"
                content.append(Paragraph(bullet_text, styles['bullet']))