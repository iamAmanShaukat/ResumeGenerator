from typing import List, Dict, Any
from reportlab.platypus import Paragraph
from .base_builder import BaseBuilder

class EducationBuilder(BaseBuilder):
    @staticmethod
    def add_education(content: List, education: List[Dict[str, Any]], styles: Dict) -> None:
        """Add education section."""
        if not education:
            return

        content.append(Paragraph("Education", styles['section_header']))
        content.append(BaseBuilder.create_section_divider())

        for edu in education:
            # Institution and degree on same line
            institution = edu.get('institution', '')
            degree = edu.get('degree', '')

            if institution and degree:
                edu_header = f"<b>{institution}</b> - {degree}"
            elif institution:
                edu_header = f"<b>{institution}</b>"
            elif degree:
                edu_header = degree
            else:
                continue

            content.append(Paragraph(edu_header, styles['education_header']))

            # Additional details
            details = []
            if edu.get('gpa') or edu.get('cgpa'):
                gpa = edu.get('gpa') or edu.get('cgpa')
                details.append(f"GPA: {gpa}")
            if edu.get('duration'):
                details.append(edu['duration'])
            if edu.get('location'):
                details.append(edu['location'])

            if details:
                content.append(Paragraph(" | ".join(details), styles['education_details']))

    @staticmethod
    def add_relevant_coursework(content: List, coursework: List[str], styles: Dict) -> None:
        """Add relevant coursework section."""
        if coursework:
            content.append(Paragraph("Relevant Coursework", styles['section_header']))
            content.append(BaseBuilder.create_section_divider())
            coursework_text = ", ".join(coursework)
            content.append(Paragraph(coursework_text, styles['normal']))