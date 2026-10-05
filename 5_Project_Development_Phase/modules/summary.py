from gemini_client import generate_text

from modules.common import (
    user_friendly_error
)


def summarize_text(
    text: str
) -> str:

    prompt = f"""
Summarize the following educational
passage for quick revision.

Requirements:

- Keep the main facts.
- Keep important terminology.
- Remove repetition.
- Use simple language.
- Do not add unsupported information.
- Make the summary easy for a student to revise.

Passage:

{text}
"""


    try:

        return generate_text(

            prompt,

            system_instruction=(
                "You are an academic summarizer "
                "focused on clarity and factual accuracy."
            )
        )

    except Exception as exc:

        return user_friendly_error(
            exc
        )