# Phase 6 – Project Testing

## 1. Objective
Verify that each module and endpoint behaves correctly, handles invalid input, and returns well-formed output.

## 2. Automated Tests (pytest)
Run from this folder:
```bash
pip install pytest
pytest
```
`conftest.py` adds the Phase 5 folder to the import path.

| File | Test | Checks |
|---|---|---|
| `test_modules.py` | `test_qna_uses_gemini` | Q&A returns the (mocked) model text |
| `test_modules.py` | `test_summary_uses_gemini` | Summary returns the (mocked) model text |
| `test_quiz.py` | `test_quiz_parsing` | Quiz JSON parses; 3 questions; 4 options each |

Gemini calls are mocked, so tests need no API key.

## 3. Manual Test Cases
| ID | Feature | Input | Expected Result | Status |
|---|---|---|---|---|
| TC01 | Q&A | "What is the difference between RAM and ROM?" | Direct, simple answer | ☐ |
| TC02 | Explain | "Pythagoras theorem" | Definition, key points, example, recap | ☐ |
| TC03 | Quiz | Photosynthesis paragraph | 3 MCQs, 4 options each | ☐ |
| TC04 | Quiz UI | Click an option | Correct/incorrect feedback shown | ☐ |
| TC05 | Summarize | AI paragraph | Short revision summary | ☐ |
| TC06 | Learning path | "Python programming" | Beginner→advanced plan, 4-week timeline | ☐ |
| TC07 | Empty input | "" | 422 validation error / no request sent | ☐ |
| TC08 | Over-length input | > 12,000 chars | Rejected by validation | ☐ |
| TC09 | Missing API key | No `GEMINI_API_KEY` | Friendly "not configured" message | ☐ |
| TC10 | Health check | `GET /health` | `{"status":"ok","service":"EduGenie"}` | ☐ |
| TC11 | Copy button | Click Copy | Result copied to clipboard | ☐ |
| TC12 | Invalid quiz JSON | Mock bad JSON | Error object returned, no crash | ☐ |

Fill the Status column (Pass / Fail) after running each case.

## 4. Suggested Additional Tests
Endpoint tests with FastAPI `TestClient`, explanation module (empty topic and local mode), `clean_json_block`, and schema validation limits.
