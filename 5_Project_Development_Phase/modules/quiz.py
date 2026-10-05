import json

from pydantic import ValidationError

from gemini_client import (
    generate_structured
)

from modules.common import (
    user_friendly_error
)

from schemas import (
    QuizResponse
)


def clean_json_block(
    text: str
) -> str:

    text = text.strip()

    if text.startswith("```"):

        lines = text.splitlines()

        if lines:

            lines = lines[1:]


        if lines and (
            lines[-1].strip()
            == "```"
        ):

            lines = lines[:-1]


        text = "\n".join(
            lines
        ).strip()


    return text


def generate_quiz(
    content: str
) -> dict:

    prompt = f"""
Create exactly 3 multiple-choice
questions from the educational content
below.

Rules:

- Create exactly 3 questions.
- Every question must contain exactly 4 options.
- There must be exactly one correct answer.
- Include a short explanation.
- Questions must be based only on the supplied content.
- Make incorrect options plausible.
- Do not add unrelated facts.

Educational content:

{content}
"""


    try:

        raw = generate_structured(

            prompt,

            QuizResponse
        )


        cleaned = clean_json_block(
            raw
        )


        data = json.loads(
            cleaned
        )


        quiz = QuizResponse.model_validate(
            data
        )


        return quiz.model_dump()


    except (
        json.JSONDecodeError,
        ValidationError
    ) as exc:

        return {

            "error": (
                "The quiz response "
                "could not be validated."
            ),

            "details": str(exc)
        }


    except Exception as exc:

        return {

            "error": user_friendly_error(
                exc
            )
        }