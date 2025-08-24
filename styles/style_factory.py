from typing import Dict

from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT, TA_JUSTIFY
from .constants import Colors

class StyleFactory:
    @staticmethod
    def create_styles() -> Dict[str, ParagraphStyle]:
        """Create comprehensive custom styles for different resume sections."""
        base_styles = getSampleStyleSheet()

        return {
            'name': ParagraphStyle(
                name='Name',
                fontSize=24,
                leading=28,
                alignment=TA_CENTER,
                spaceAfter=8,
                fontName='Helvetica-Bold',
                textColor=Colors.PRIMARY
            ),
            'contact': ParagraphStyle(
                name='Contact',
                fontSize=10,
                leading=12,
                alignment=TA_CENTER,
                spaceAfter=20,
                fontName='Helvetica',
                textColor=Colors.SECONDARY
            ),
            'section_header': ParagraphStyle(
                name='SectionHeader',
                fontSize=14,
                leading=16,
                spaceBefore=20,
                spaceAfter=10,
                fontName='Helvetica-Bold',
                textColor=Colors.PRIMARY
            ),
            'subsection_header': ParagraphStyle(
                name='SubsectionHeader',
                fontSize=11,
                leading=13,
                spaceBefore=8,
                spaceAfter=4,
                fontName='Helvetica-Bold',
                textColor=Colors.BLACK
            ),
            'job_title': ParagraphStyle(
                name='JobTitle',
                fontSize=12,
                leading=14,
                spaceBefore=8,
                spaceAfter=2,
                fontName='Helvetica-Bold',
                textColor=Colors.ACCENT
            ),
            'company_info': ParagraphStyle(
                name='CompanyInfo',
                fontSize=10,
                leading=12,
                spaceAfter=6,
                fontName='Helvetica-Oblique',
                textColor=Colors.SECONDARY
            ),
            'normal': ParagraphStyle(
                name='Normal',
                fontSize=10,
                leading=12,
                spaceAfter=4,
                fontName='Helvetica',
                alignment=TA_JUSTIFY
            ),
            'bullet': ParagraphStyle(
                name='Bullet',
                fontSize=10,
                leading=12,
                leftIndent=20,
                firstLineIndent=-15,
                spaceAfter=3,
                fontName='Helvetica',
                bulletFontName='Helvetica',
                bulletIndent=15,
                alignment=TA_JUSTIFY
            ),
            'skills': ParagraphStyle(
                name='Skills',
                fontSize=10,
                leading=12,
                spaceAfter=4,
                fontName='Helvetica',
                leftIndent=10
            ),
            'education_header': ParagraphStyle(
                name='EducationHeader',
                fontSize=11,
                leading=13,
                spaceBefore=6,
                spaceAfter=2,
                fontName='Helvetica-Bold'
            ),
            'education_details': ParagraphStyle(
                name='EducationDetails',
                fontSize=10,
                leading=12,
                spaceAfter=4,
                fontName='Helvetica',
                textColor=Colors.SECONDARY
            )
        }