# Phase 4 – Project Planning

## 1. Team & Roles
| Member | Role | Responsibility |
|---|---|---|
| [Name] | Team Leader | Coordination, submission |
| [Name] | Backend | FastAPI routes, Gemini client |
| [Name] | Frontend | HTML/CSS/JS UI |
| [Name] | Testing & Docs | Test cases, documentation |

## 2. Timeline
| Week | Phase | Deliverable |
|---|---|---|
| 1 | Brainstorming & Requirements | Problem statement, feature list, requirements |
| 2 | Design & Planning | Architecture, API design, plan |
| 3 | Development | Working backend + UI |
| 4 | Testing & Documentation | Test report, final docs |
| 5 | Demonstration | Demo, README, final submission |

## 3. Milestones
- [ ] M1 – Requirements approved
- [ ] M2 – Design finalised
- [ ] M3 – All 5 endpoints working
- [ ] M4 – UI integrated
- [ ] M5 – Tests passing
- [ ] M6 – Documentation and demo ready

## 4. Risks & Mitigation
| Risk | Mitigation |
|---|---|
| Gemini API key missing / quota exhausted | Clear error message; `.env.example`; local explanation mode |
| Invalid quiz JSON from model | Structured schema + Pydantic validation + error response |
| Inaccurate AI output | Prompts forbid invented facts; user advised to verify |
| Long input | 12,000-character limit |

## 5. Tools
Python, FastAPI, VS Code, GitHub, Postman/browser, pytest.
