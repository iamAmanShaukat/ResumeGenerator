from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate
from typing import Dict, List, Any

from builders.achievements_builder import AchievementsBuilder
from builders.education_builder import EducationBuilder
from builders.experience_builder import ExperienceBuilder
from builders.header_builder import HeaderBuilder
from builders.projects_builder import ProjectsBuilder
from builders.skills_builder import SkillsBuilder
from styles.style_factory import StyleFactory
from validators.json_validator import JsonValidator


class ProfessionalResumeGenerator:
    def __init__(self):
        self.styles = StyleFactory.create_styles()
        self.json_validator = JsonValidator()

    def create_resume(self, json_str: str, output_filename: str = "professional_resume.pdf") -> bool:
        """
        Args:
            json_str: JSON string containing resume data
            output_filename: Output PDF filename

        Returns:
            bool: True if successful, False otherwise
        """
        try:
            # Parse and validate JSON
            data = self.json_validator.validate_json_data(json_str)

            # Initialize PDF document with professional margins
            doc = SimpleDocTemplate(
                output_filename,
                pagesize=letter,
                leftMargin=0.75 * inch,
                rightMargin=0.75 * inch,
                topMargin=0.75 * inch,
                bottomMargin=0.75 * inch
            )

            content = []

            # Add sections in professional order
            HeaderBuilder.add_header(content, data, self.styles)
            EducationBuilder.add_education(content, data.get('education', []), self.styles)
            EducationBuilder.add_relevant_coursework(content, data.get('relevant_coursework', []), self.styles)
            ExperienceBuilder.add_experience(content, data.get('experience', []), "Professional Experience", self.styles)
            ExperienceBuilder.add_experience(content, data.get('other_experience', []), "Additional Experience", self.styles)
            SkillsBuilder.add_skills(content, data.get('technical_skills', {}), self.styles)
            ProjectsBuilder.add_projects(content, data.get('projects', []), self.styles)
            AchievementsBuilder.add_achievements(content, data.get('achievements', []), self.styles)

            # Build PDF
            doc.build(content)
            print(f"Professional resume generated successfully: {output_filename}")
            return True

        except Exception as e:
            print(f"Error generating resume: {str(e)}")
            return False