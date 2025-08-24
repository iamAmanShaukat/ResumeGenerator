import json
import os

from llm.resume_updater import ResumeUpdater


class JobDescriptionHandler:
    """Class to handle job description loading and resume updating with LLM."""

    def __init__(self):
        pass
    def _load_api_key(self) -> str:
        """Load Gemini API key from config.json."""
        try:
            with open('config.json', 'r') as f:
                config = json.load(f)
                api_key = config.get('GEMINI_API_KEY')
                if not api_key:
                    print("⚠️ Warning: GEMINI_API_KEY not found in config.json.")
                    return None
                return api_key
        except FileNotFoundError:
            print("⚠️ Warning: config.json not found.")
            return None
        except json.JSONDecodeError as e:
            print(f"⚠️ Warning: Error parsing config.json: {str(e)}.")
            return None
        except Exception as e:
            print(f"⚠️ Warning: Error reading config.json: {str(e)}.")
            return None

    def process_job_description(self, resume_json: str) -> str:
        """
        Load job description, update resume using LLM, and return JSON string to use.
        Falls back to original resume JSON if job description or LLM update fails.
        """
        # Attempt to load job description
        try:
            with open('job_description.txt', 'r') as f:
                job_desc = f.read()
        except FileNotFoundError:
            print("⚠️ Warning: job_description.txt not found. Skipping LLM update and using original resume.")
            return resume_json
        except Exception as e:
            print(f"⚠️ Warning: Error reading job_description.txt: {str(e)}. Skipping LLM update and using original resume.")
            return resume_json

        # Check for API key and proceed with LLM update
        api_key = self._load_api_key()
        if not api_key:
            print("⚠️ Warning: GEMINI_API_KEY environment variable not set. Skipping LLM update and using original resume.")
            return resume_json

        try:
            updater = ResumeUpdater(api_key)
            updated_dict = updater.update_resume(job_desc, resume_json)
            with open('updated_json_resume.json', 'w') as f:
                json.dump(updated_dict, f, indent=4)
            print("✅ Updated resume JSON saved to updated_json_resume.json")
            return json.dumps(updated_dict)
        except Exception as e:
            print(f"❌ Error during LLM resume update: {str(e)}. Falling back to original resume.")
            return resume_json