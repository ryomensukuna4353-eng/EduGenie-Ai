# EduGenie – Project Report

## 1. Abstract
EduGenie is a web-based AI learning assistant built with FastAPI and Google Gemini. It provides question answering, topic explanation, quiz generation, text summarization, and personalised learning paths through a single simple interface.

## 2. Introduction
Students need fast, simple, and structured help while studying. EduGenie combines five learning tools in one application using carefully designed prompts and validated outputs.

## 3. Objectives
- Provide beginner-friendly answers and explanations
- Generate self-test quizzes from any study content
- Produce revision summaries and study plans
- Keep the application simple, secure, and easy to run

## 4. System Overview
See Phase 3 (design) for architecture and sequence diagrams. Requests flow from the browser to FastAPI, through Pydantic validation, to a task module that calls Gemini and returns the result.

## 5. Implementation Summary
| Module | Description |
|---|---|
| Q&A | Direct answer first, simple reasoning, no invented sources |
| Explanation | Definition, main idea, 3 key points, example, recap (Gemini or local model) |
| Quiz | Exactly 3 MCQs × 4 options, validated with Pydantic |
| Summary | Keeps facts and terms, removes repetition |
| Learning Path | Prerequisites, levels, 4-week timeline, practice, revision, readiness checklist |

## 6. Testing Summary
See Phase 6. Automated pytest tests cover Q&A, summary, and quiz parsing; manual test cases cover all features and error handling.

## 7. Limitations
- Depends on the Gemini API and internet
- AI output can be inaccurate
- No login, history, or progress tracking

## 8. Future Scope
User accounts and history, voice input, PDF/notes upload, progress dashboard, multi-language support, quiz scoring.

## 9. Conclusion
EduGenie shows how generative AI can be packaged into a practical study companion with a small, maintainable codebase.
