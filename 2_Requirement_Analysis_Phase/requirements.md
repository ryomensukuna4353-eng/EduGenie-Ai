# Phase 2 – Requirement Analysis

## 1. Functional Requirements
| ID | Requirement | Endpoint |
|---|---|---|
| FR1 | User can ask an academic question and receive a concise answer | `POST /qa` |
| FR2 | User can request a beginner explanation of a topic | `POST /explain` |
| FR3 | User can generate a 3-question MCQ quiz from supplied content | `POST /quiz` |
| FR4 | User can summarize a passage for revision | `POST /summarize` |
| FR5 | User can get a learning path for a topic | `POST /learn/recommendations` |
| FR6 | UI lets user choose task, load an example, submit, and copy result | `GET /` |
| FR7 | Quiz options are clickable with correct/incorrect feedback | Frontend |
| FR8 | Service health can be checked | `GET /health` |

## 2. Non-Functional Requirements
- **Usability:** simple one-page interface, example input provided
- **Reliability:** errors are returned as friendly messages, not stack traces
- **Security:** API key kept in `.env`, never in code; HTML output is escaped to prevent XSS
- **Input limits:** max 12,000 characters (configurable); empty input rejected
- **Performance:** response time depends on Gemini; output capped at 1,200 tokens
- **Portability:** runs on any machine with Python 3.10+

## 3. User Stories
1. As a student, I want a short, clear answer so I can clear a doubt quickly.
2. As a student, I want a topic explained simply so I can understand it as a beginner.
3. As a student, I want a quiz from my notes so I can test myself.
4. As a student, I want a summary so I can revise faster.
5. As a student, I want a learning plan so I know what to study and in what order.

## 4. Technology Stack
| Layer | Technology |
|---|---|
| Backend | Python, FastAPI, Uvicorn |
| AI | Google Gemini (`gemini-2.5-flash`) via `google-genai`; optional local Hugging Face model |
| Validation | Pydantic v2 |
| Frontend | HTML, CSS, JavaScript (Jinja2 template) |
| Testing | pytest, `unittest.mock` |

## 5. Hardware / Software Requirements
- Python 3.10+, internet connection, Gemini API key
- Any modern browser
- (Local mode only) `transformers` and `torch`

## 6. Constraints & Assumptions
- Needs a valid Gemini API key and internet access
- AI output may contain errors; users should verify important facts
- No user accounts or stored data in version 1.0
