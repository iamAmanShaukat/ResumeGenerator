from typing import Dict, Any, List
from reportlab.platypus import Paragraph

from utils.formatting import FormattingUtils
from .base_builder import BaseBuilder

class HeaderBuilder(BaseBuilder):
    @staticmethod
    def add_header(content: List, data: Dict[str, Any], styles: Dict) -> None:
        """Add professional header with name and contact info."""
        # Name
        content.append(Paragraph(data['name'], styles['name']))

        # Contact information
        contact_text = FormattingUtils.format_contact_info(data)
        if contact_text:
            content.append(Paragraph(contact_text, styles['contact']))

        # Professional summary if available
        if data.get('summary'):
            content.append(Paragraph("Professional Summary", styles['section_header']))
            content.append(BaseBuilder.create_section_divider())
            content.append(Paragraph(data['summary'], styles['normal']))