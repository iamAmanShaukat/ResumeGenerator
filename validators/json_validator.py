import json
import re
from typing import Dict, Any

class JsonValidator:
    @staticmethod
    def validate_json_data(json_str: str) -> Dict[str, Any]:
        """Validate and clean JSON data."""
        try:
            data = json.loads(json_str)
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON format: {str(e)}")

        required_fields = ['name']
        for field in required_fields:
            if field not in data or not data[field]:
                raise ValueError(f"Required field '{field}' is missing or empty")

        # Clean and validate email
        if 'email' in data and data['email']:
            email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
            if not re.match(email_pattern, data['email']):
                print(f"Warning: Invalid email format: {data['email']}")

        return data