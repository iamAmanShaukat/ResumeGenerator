import json
import google.generativeai as genai
from typing import Dict

class ResumeUpdater:
    """Class to update resume JSON using Gemini LLM."""

    def __init__(self, api_key: str):
        try:
            genai.configure(api_key=api_key)
            self.model = genai.GenerativeModel('gemini-1.5-flash')
            print("Gemini model initialized successfully.")
        except Exception as e:
            print(f"Error initializing Gemini: {str(e)}")
            raise

    def update_resume(self, job_desc: str, resume_json: str) -> Dict:
        """Update resume JSON based on job description using LLM."""
        prompt = f"""
Given the following job description:

{job_desc}

And the following resume in JSON format:

{resume_json}

Please update the resume to better tailor it to the job description. Possible updates include:
- Revising the professional summary to emphasize relevant skills and experiences.
- Adjusting experience descriptions to include keywords from the job description.
- Reordering or adding skills that match the job requirements.
- Modifying project descriptions to highlight applicable aspects.
- Ensuring the overall structure remains similar, but optimized for the job.

Output ONLY the updated JSON object, with no additional text, explanations, or markdown. Ensure the output is valid JSON.
"""

        try:
            print("Sending request to Gemini for resume update...")
            response = self.model.generate_content(prompt)
            updated_text = response.text.strip()

            # Remove potential mark down code blocks
            if updated_text.startswith('```json'):
                updated_text = updated_text[7:].strip()
            if updated_text.endswith('```'):
                updated_text = updated_text[:-3].strip()

            updated_dict = json.loads(updated_text)
            print("Resume updated successfully by LLM.")
            return updated_dict
        except json.JSONDecodeError as e:
            print(f"Error parsing LLM response as JSON: {str(e)}")
            raise ValueError("Invalid JSON in LLM response.")
        except Exception as e:
            print(f"Error generating content with Gemini: {str(e)}")
            raise