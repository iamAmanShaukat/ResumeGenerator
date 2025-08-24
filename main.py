# resume_generator/main.py
from core.resume_generator import ProfessionalResumeGenerator
import json
import re

from llm.job_description_handler import JobDescriptionHandler


def main():
    # Load JSON data from file
    try:
        with open('json_resume.json', 'r') as file:
            json_resume = file.read()
    except FileNotFoundError:
        print("Error: json_resume.json not found.")
        return
    except Exception as e:
        print(f"Error reading json_resume.json: {str(e)}")
        return

        # Parse JSON to extract name for filename
    try:
        data = json.loads(json_resume)
        name = data.get('name', 'resume').lower()
        # Clean name for filename: replace spaces and special characters
        cleaned_name = re.sub(r'[^a-z0-9]+', '_', name.strip())
        output_filename = f"{cleaned_name}_resume.pdf"
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON: {str(e)}")
        return

    # Handle job description and resume update
    job_handler = JobDescriptionHandler()
    json_to_use = job_handler.process_job_description(json_resume)

    generator = ProfessionalResumeGenerator()
    success = generator.create_resume(json_to_use, output_filename)

    print(f"Resume generation {success}")


if __name__ == "__main__":
    main()