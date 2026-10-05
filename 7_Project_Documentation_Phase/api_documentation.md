# EduGenie – API Documentation

Interactive docs are also available at `/docs` (Swagger UI) when the server is running.

**Request body (all POST routes):** `{"text": "your input"}` (1–12,000 characters)

| Route | Description | Success response |
|---|---|---|
| `GET /health` | Health check | `{"status":"ok","service":"EduGenie"}` |
| `POST /qa` | Answer a question | `{"result": "<text>"}` |
| `POST /explain` | Explain a topic | `{"result": "<text>"}` |
| `POST /summarize` | Summarize text | `{"result": "<text>"}` |
| `POST /learn/recommendations` | Learning path | `{"result": "<text>"}` |
| `POST /quiz` | 3-question MCQ quiz | `{"questions":[{"question","options","correct_answer","explanation"}]}` |

**Errors:** invalid input returns HTTP 422. AI/config failures return a message starting with "EduGenie could not complete the request:" (quiz returns `{"error": "..."}`).

**Example**
```bash
curl -X POST http://127.0.0.1:8000/qa -H "Content-Type: application/json" -d '{"text":"What is RAM?"}'
```

## Configuration (`.env`)
| Variable | Default | Purpose |
|---|---|---|
| `GEMINI_API_KEY` | – | Required for Gemini mode |
| `GEMINI_MODEL` | `gemini-2.5-flash` | Model name |
| `EXPLANATION_MODE` | `gemini` | `gemini` or `local` |
| `LOCAL_EXPLANATION_MODEL` | `MBZUAI/LaMini-Flan-T5-783M` | Local model |
| `MAX_INPUT_CHARS` | `12000` | Input limit |
| `MAX_OUTPUT_TOKENS` | `1200` | Output limit |
| `TEMPERATURE` | `0.4` | Creativity |
