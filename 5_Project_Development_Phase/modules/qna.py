from gemini_client import generate_text

from modules.common import (
    user_friendly_error
)


def answer_question(
    question: str
) -> str:

    prompt = f"""
You are EduGenie, a student-friendly
educational assistant.

Answer the student's question accurately
and concisely.

Rules:

- Start with the direct answer.
- Explain important reasoning in simple language.
- Use short examples when helpful.
- If the question is ambiguous, state the assumption.
- Do not invent sources or citations.
- Keep the answer educational and easy to understand.

Student question:

{question}
"""

    try:

        return generate_text(

            prompt,

            system_instruction=(
                "You are a clear and patient "
                "academic tutor. "
                "Prefer simple language."
            )
        )

    except Exception as exc:

        return user_friendly_error(
            exc
        )