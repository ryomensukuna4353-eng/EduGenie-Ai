# Phase 1 – Brainstorming & Ideation

**Project:** EduGenie – AI Learning Assistant (FastAPI + Google Gemini)
**Team:** [Team name] | **Members:** [Add names]

## 1. Problem Statement
Students often struggle to (a) get quick, simple answers to doubts, (b) understand difficult topics, (c) revise long passages, (d) test themselves, and (e) decide what to study next. Information is scattered across many websites and is rarely written at a beginner's level.

## 2. Idea
A single web app where a student picks a task, types a question/topic/passage, and gets an AI-generated result written in easy English.

## 3. Brainstormed Features
| Feature | Student need | Selected? |
|---|---|---|
| Ask a Question (Q&A) | Quick doubt clearing | Yes |
| Explain a Topic | Beginner-friendly understanding | Yes |
| Generate Quiz (3 MCQs) | Self-testing | Yes |
| Summarize Text | Fast revision | Yes |
| Learning Path | Structured 4-week plan | Yes |
| Voice input, user login, progress dashboard | Convenience / tracking | Future scope |

## 4. Empathy Map (Target User: college student)
- **Says:** "I don't understand this topic", "I need notes before the exam."
- **Thinks:** "Where do I start?", "Am I ready for the test?"
- **Does:** Searches many sites, watches videos, copies notes.
- **Feels:** Overwhelmed, short on time.

## 5. Proposed Solution
A lightweight FastAPI backend that sends carefully designed prompts to Google Gemini, with a simple one-page UI. Optional local model mode (Hugging Face LaMini-Flan-T5) for explanations without the Gemini API.

## 6. Expected Outcomes
- One place for five learning tasks
- Simple, structured, student-friendly output
- Validated quiz output (exactly 3 questions × 4 options)
