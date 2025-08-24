# Professional Resume Generator 📄✨

A Python-based tool to generate professional, customizable resumes in **PDF format** from structured JSON data. Optionally leverage the power of AI with **Google's Gemini LLM** to tailor your resume to specific job descriptions.

---

## ✅ Features

- **Professional PDF Output**: Clean, well-formatted resumes using `ReportLab`, with support for custom fonts, colors, and styling.
- **Structured JSON Input**: Define your resume in `json_resume.json` for easy editing and reuse.
- **Modular Architecture**: Clean separation of concerns with dedicated modules for building, styling, validation, utilities, and AI integration.
- **AI Resume Tailoring (Gemini LLM)**: Automatically refine your summary, experience, and skills to match a job description using Google’s Gemini API.
- **Dynamic Filenames**: PDFs are named after the candidate (e.g., `aman_shaukat_resume.pdf`).
- **Robust Error Handling**: Graceful fallbacks on JSON errors, file issues, or LLM failures — defaults to original resume if tailoring fails.
- **Secure Configuration**: API keys stored in `config.json`, safely excluded via `.gitignore`.

---

## 🗂️ Project Structure

```bash
resumeGenerator/
├── main.py                     # Entry point
├── requirements.txt            # Dependencies
├── .gitignore                  # Excludes config & generated files
├── config.json                 # Stores GEMINI_API_KEY (not tracked)
├── json_resume.json            # Resume input data
├── job_description.txt         # Optional: job posting for AI tailoring
├── updated_json_resume.json    # Output: AI-updated resume (auto-generated)
└── resume_generator/
    ├── __init__.py
    ├── core/
    │   └── resume_generator.py # Main logic
    ├── builders/
    │   ├── base_builder.py
    │   ├── header_builder.py
    │   ├── education_builder.py
    │   ├── experience_builder.py
    │   ├── skills_builder.py
    │   ├── projects_builder.py
    │   └── achievements_builder.py
    ├── styles/
    │   ├── style_factory.py    # Dynamic styling
    │   └── constants.py        # Fonts, colors, layout settings
    ├── validators/
    │   └── json_validator.py   # Validates JSON schema
    ├── utils/
    │   ├── formatting.py       # Text & date utilities
    │   └── table.py            # Table formatting helpers
    └── llm/
        ├── resume_updater.py           # Updates resume via Gemini
        └── job_description_handler.py  # Parses job description
```

---

## ⚙️ Prerequisites

- **Python 3.8+**
- **Gemini API Key** *(optional, for AI tailoring)*  
  Get one at: [https://ai.google.dev/](https://ai.google.dev/)

---

## 🔧 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/resumeGenerator.git
cd resumeGenerator
```

### 2. Set Up Virtual Environment (Recommended)

```bash
python -m venv .venv
source .venv/bin/activate    # On Windows: .venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure API Key

Create `config.json` in the root directory:

```json
{
  "GEMINI_API_KEY": "your-gemini-api-key-here"
}
```

> 🔒 **Important**: This file is already in `.gitignore`. Never commit it!

### 5. Prepare Input Files

- ✅ Ensure `json_resume.json` exists with your resume data.
- 📝 *(Optional)* Add a `job_description.txt` to enable AI tailoring.

> 💡 A sample `json_resume.json` is included in the repo.

---

## ▶️ Usage

Run the generator:

```bash
python main.py
```

### What Happens?

- Reads `json_resume.json`.
- If `job_description.txt` exists and `GEMINI_API_KEY` is valid:
  - Uses **Gemini LLM** to tailor your resume.
  - Saves updated version to `updated_json_resume.json`.
- Generates a PDF (e.g., `aman_shaukat_resume.pdf`) in the project root.

> 🚫 No job description? Falls back to standard generation.

---

## 📄 Example `json_resume.json`

```json
{
  "name": "Aman Shaukat",
  "location": "London, UK",
  "email": "iamAmanShaukat@gmail.com",
  "phone": "+44 7123 456789",
  "summary": "Experienced software engineer...",
  "experience": [
    {
      "title": "Software Developer",
      "company": "TechCorp Ltd",
      "start_date": "Jan 2020",
      "end_date": "Present",
      "responsibilities": ["Developed APIs", "Led team projects"]
    }
  ],
  "education": [
    {
      "degree": "BSc Computer Science",
      "institution": "University of London",
      "graduation_date": "2019"
    }
  ],
  "skills": ["Python", "Django", "AWS", "Git"],
  "projects": [
    {
      "name": "Resume Generator",
      "description": "Built a tool to auto-generate tailored resumes."
    }
  ],
  "achievements": ["Employee of the Year 2022"]
}
```

---

## 📝 Example `job_description.txt` (Optional)

```
We are seeking a Software Engineer with strong Python and Django experience, 
familiarity with cloud platforms (AWS/GCP), and a passion for clean code and automation.
```

> The AI will use this to optimize your resume content accordingly.

---

## ❗ Error Handling

| Issue | Behavior |
|------|--------|
| Missing `json_resume.json` | Logs warning and exits |
| Invalid JSON format | Catches parsing errors, shows line number if possible |
| Missing or invalid `config.json` | Skips AI step; proceeds with base resume |
| Gemini API failure | Falls back to original resume data |
| Missing `job_description.txt` | Skips AI tailoring, uses original JSON |

---

## 📦 Dependencies

```txt
reportlab==4.0.8          # PDF generation
google-generativeai==0.5.0 # Gemini LLM integration
```

> Optional: Use `python-dotenv` to load from `.env` instead of `config.json`.

---

## 🛡️ Security Notes

- Never commit `config.json` or `.env` files.
- Use environment variables in production.
- Validate all inputs before deployment.

---

## 🎨 Customization

- ✏️ Edit `json_resume.json` to update your information.
- 🎨 Modify styles in `resume_generator/styles/constants.py` and `style_factory.py` to change fonts, colors, layout.
- ➕ Add new sections by creating additional builder classes (e.g., `certifications_builder.py`).

---

## 🤖 LLM Tailoring

Uses **Google Gemini** to:
- Rewrite your professional summary
- Optimize bullet points in experience
- Highlight relevant skills
- Align keywords with the job description

> ✅ Requires internet + valid API key  
> 🚫 Remove `job_description.txt` to skip AI processing

---

## 🔄 Extensibility

The modular design makes it easy to:
- Add new resume sections
- Support additional LLMs (e.g., OpenAI, Anthropic)
- Export to other formats (e.g., HTML, DOCX)
- Integrate with web interfaces or CLI tools

---

## 📜 License

This project is licensed under the **MIT License**.  
See [LICENSE](LICENSE) for details.

---

## 📬 Contact

For questions, feedback, or collaboration:

📧 **Email**: [iamAmanShaukat@gmail.com](mailto:iamAmanShaukat@gmail.com)  

---

🚀 Turn your resume into a targeted, professional document — automatically.  
