# Phase 5 – Project Development

This folder contains the complete working application.

## Structure
```
5_Project_Development_Phase/
├── main.py               # FastAPI routes
├── config.py             # Settings from .env
├── schemas.py            # Request/response validation
├── gemini_client.py      # Gemini API wrapper
├── modules/              # qna, explanation, quiz, summary, learning_path, common
├── templates/index.html  # UI page
├── static/css/style.css
├── static/js/app.js
├── requirements.txt
└── .env.example
```

## Run locally
```bash
cd 5_Project_Development_Phase
python -m venv .venv
.venv\Scripts\activate          # Windows  (Linux/Mac: source .venv/bin/activate)
pip install -r requirements.txt
copy .env.example .env          # Linux/Mac: cp .env.example .env  -> then add GEMINI_API_KEY
uvicorn main:app --reload
```
Open http://127.0.0.1:8000

## Changes made while organising the project
- `app.js` moved from `static/css/js/` to `static/js/`, and the script path in `index.html` updated to `js/app.js`. Previously the template pointed to `static/app.js`, which did not exist, so the page buttons would not work.
- Removed `__pycache__` folders; added `.env.example` and `.gitignore`.
