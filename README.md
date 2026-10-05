# EduGenie – AI Learning Assistant

AI-powered study helper built with **FastAPI** and **Google Gemini**: ask questions, get topic explanations, generate quizzes, summarize text, and build learning paths.

## Project Structure (phase-wise)
| Phase | Folder | Contents |
|---|---|---|
| 1 | `1_Brainstorming_Ideation_Phase/` | Problem statement, ideas, empathy map |
| 2 | `2_Requirement_Analysis_Phase/` | Functional and non-functional requirements, tech stack |
| 3 | `3_Project_Design_Phase/` | Architecture, API and UI design, diagrams |
| 4 | `4_Project_Planning_Phase/` | Roles, timeline, milestones, risks |
| 5 | `5_Project_Development_Phase/` | Complete source code |
| 6 | `6_Project_Testing_Phase/` | Test plan, test cases, pytest tests |
| 7 | `7_Project_Documentation_Phase/` | Report, user manual, API docs |
| 8 | `8_Project_Demonstration_Phase/` | Demo guide, screenshots |

## Features
- Ask a Question · Explain a Topic · Generate Quiz (3 MCQs) · Summarize Text · Learning Path

## Quick Start
```bash
cd 5_Project_Development_Phase
python -m venv .venv
.venv\Scripts\activate            # Linux/Mac: source .venv/bin/activate
pip install -r requirements.txt
copy .env.example .env            # Linux/Mac: cp .env.example .env
# add your GEMINI_API_KEY to .env
uvicorn main:app --reload
```
Open http://127.0.0.1:8000 (API docs at `/docs`).

## Run Tests
```bash
cd 6_Project_Testing_Phase
pip install pytest
pytest
```

## Tech Stack
Python · FastAPI · Uvicorn · Pydantic · Jinja2 · Google Gemini (`google-genai`) · HTML/CSS/JS · pytest

## Team
[Team name] – [Member names]

## License
[Add license]
