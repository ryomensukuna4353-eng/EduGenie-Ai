from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from schemas import TaskRequest
from modules.qna import answer_question
from modules.explanation import explain_topic
from modules.quiz import generate_quiz
from modules.summary import summarize_text
from modules.learning_path import get_learning_recommendations


# Project directory
BASE_DIR = Path(__file__).resolve().parent


app = FastAPI(
    title="EduGenie - Google Gemini Powered Learning Assistant",
    version="1.0.0",
    description="AI-powered educational assistant built with FastAPI and Gemini.",
)


# -----------------------------
# STATIC FILES
# -----------------------------

app.mount(
    "/static",
    StaticFiles(directory=BASE_DIR / "static"),
    name="static"
)


# -----------------------------
# HTML TEMPLATES
# -----------------------------

templates = Jinja2Templates(
    directory=BASE_DIR / "templates"
)


# -----------------------------
# HOME PAGE
# -----------------------------

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )



# -----------------------------
# HEALTH CHECK
# -----------------------------

@app.get("/health")
async def health():
    return {
        "status": "ok",
        "service": "EduGenie"
    }


# -----------------------------
# QUESTION & ANSWER
# -----------------------------

@app.post("/qa")
async def qa(payload: TaskRequest):

    result = answer_question(
        payload.text
    )

    return {
        "result": result
    }


# -----------------------------
# EXPLANATION
# -----------------------------

@app.post("/explain")
async def explain(payload: TaskRequest):

    result = explain_topic(
        payload.text
    )

    return {
        "result": result
    }


# -----------------------------
# QUIZ
# -----------------------------

@app.post("/quiz")
async def quiz(payload: TaskRequest):

    return generate_quiz(
        payload.text
    )


# -----------------------------
# SUMMARY
# -----------------------------

@app.post("/summarize")
async def summarize(payload: TaskRequest):

    result = summarize_text(
        payload.text
    )

    return {
        "result": result
    }


# -----------------------------
# LEARNING RECOMMENDATIONS
# -----------------------------

@app.post("/learn/recommendations")
async def recommendations(payload: TaskRequest):

    result = get_learning_recommendations(
        payload.text
    )

    return {
        "result": result
    }
