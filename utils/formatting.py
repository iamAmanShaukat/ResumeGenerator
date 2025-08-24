from typing import Dict, Any

class FormattingUtils:
    @staticmethod
    def format_contact_info(data: Dict[str, Any]) -> str:
        """ CCD Format contact information with proper separators."""
        contact_parts = []

        if data.get('location'):
            contact_parts.append(data['location'])
        if data.get('phone'):
            contact_parts.append(data['phone'])
        if data.get('email'):
            contact_parts.append(f"<link href='mailto:{data['email']}'>{data['email']}</link>")
        if data.get('linkedin'):

            linkedin_url = data['linkedin'] if data['linkedin'].startswith(
                'http') else f"linkedin.com/in/{data['linkedin']}"
            contact_parts.append(f"<link href='{linkedin_url}'>LinkedIn</link>")
        if data.get('github'):
            github_url = data['github'] if data['github'].startswith('http') else f"github.com/{data['github']}"
            contact_parts.append(f"<link href='{github_url}'>GitHub</link>")

        return " • ".join(contact_parts)