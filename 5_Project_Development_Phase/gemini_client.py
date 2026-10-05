from functools import lru_cache

from google import genai
from google.genai import types

from config import (
    GEMINI_API_KEY,
    GEMINI_MODEL,
    MAX_OUTPUT_TOKENS,
    TEMPERATURE,
)


class GeminiConfigurationError(
    RuntimeError
):
    pass


@lru_cache(maxsize=1)
def get_client():

    if not GEMINI_API_KEY:

        raise GeminiConfigurationError(
            "GEMINI_API_KEY is not configured. "
            "Please add it to your .env file."
        )

    return genai.Client(
        api_key=GEMINI_API_KEY
    )


def generate_text(
    prompt: str,
    system_instruction: str | None = None
) -> str:

    client = get_client()

    config = types.GenerateContentConfig(

        temperature=TEMPERATURE,

        max_output_tokens=MAX_OUTPUT_TOKENS,

        system_instruction=system_instruction,
    )

    response = client.models.generate_content(

        model=GEMINI_MODEL,

        contents=prompt,

        config=config,
    )

    text = getattr(
        response,
        "text",
        None
    )

    if not text:

        raise RuntimeError(
            "Gemini returned an empty response."
        )

    return text.strip()


def generate_structured(
    prompt: str,
    schema
):

    client = get_client()

    config = types.GenerateContentConfig(

        temperature=0.3,

        max_output_tokens=MAX_OUTPUT_TOKENS,

        response_mime_type="application/json",

        response_schema=schema,
    )

    response = client.models.generate_content(

        model=GEMINI_MODEL,

        contents=prompt,

        config=config,
    )

    text = getattr(
        response,
        "text",
        None
    )

    if not text:

        raise RuntimeError(
            "Gemini returned an empty response."
        )

    return text