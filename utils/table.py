from typing import List
from reportlab.lib.units import inch
from reportlab.platypus import Table, TableStyle


class TableUtils:
    @staticmethod
    def calculate_optimal_column_widths(skills_data: List[List[str]], available_width: float = 6.5) -> List[float]:
        """Calculate optimal column widths based on content length."""
        if not skills_data:
            return [2 * inch, 4.5 * inch]

        # Find the longest category name and skills text
        max_category_length = max(len(row[0]) for row in skills_data) if skills_data else 20
        max_skills_length = max(len(row[1]) for row in skills_data) if skills_data else 50

        # Calculate proportional widths (minimum 1.2 inches for category)
        category_width = max(1.2 * inch, min(2.5 * inch, (max_category_length * 0.1 + 1.2) * inch))
        skills_width = available_width * inch - category_width
        return [category_width, skills_width]

    @staticmethod
    def create_skills_table(skills_data: List[List[str]]) -> Table:
        """Create a skills table with dynamic column widths."""
        col_widths = TableUtils.calculate_optimal_column_widths(skills_data)
        skills_table = Table(skills_data, colWidths=col_widths)
        skills_table.setStyle(TableStyle([
            ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
            ('FONTNAME', (1, 0), (1, -1), 'Helvetica'),
            ('FONTSIZE', (0, 0), (-1, -1), 10),
            ('VALIGN', (0, 0), (-1, -1), 'TOP'),
            ('LEFTPADDING', (0, 0), (-1, -1), 0),
            ('RIGHTPADDING', (0, 0), (-1, -1), 8),
            ('TOPPADDING', (0, 0), (-1, -1), 3),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
            ('WORDWRAP', (1, 0), (1, -1), True),
        ]))
        skills_table.hAlign = 'LEFT'
        return skills_table