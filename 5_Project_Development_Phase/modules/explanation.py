from config import EXPLANATION_MODE, LOCAL_EXPLANATION_MODEL
from gemini_client import generate_text
from modules.common import user_friendly_error


_local_pipeline = None


def _local_explain(topic: str) -> str:
    """
    Generate an explanation using a local Hugging Face model.
    Used only when EXPLANATION_MODE is set to 'local'.
    """

    global _local_pipeline

    try:
        from transformers import pipeline
    except ImportError as exc:
        raise RuntimeError(
            "Local explanation mode requires transformers and torch. "
            "Run: pip install transformers torch"
        ) from exc

    try:
        if _local_pipeline is None:
            _local_pipeline = pipeline(
                "text2text-generation",
                model=LOCAL_EXPLANATION_MODEL
            )
    except Exception as exc:
        raise RuntimeError(
            f"Could not load the local explanation model "
            f"'{LOCAL_EXPLANATION_MODEL}'. "
            f"Check the model name and your internet connection."
        ) from exc

    prompt = f"""
Explain the following educational topic for a beginner.

Give:
1. Simple definition
2. Main idea
3. Three key points
4. One simple example
5. One-line recap

Topic:
{topic}

Use easy English.
Avoid unnecessary technical jargon.
"""

    try:
        result = _local_pipeline(
            prompt,
            max_new_tokens=350
        )
    except Exception as exc:
        raise RuntimeError(
            "The local explanation model failed while generating the answer."
        ) from exc

    if not result:
        raise RuntimeError(
            "The local explanation model returned no result."
        )

    generated_text = result[0].get("generated_text", "")

    if not generated_text:
        raise RuntimeError(
            "The local explanation model returned empty text."
        )

    return generated_text.strip()


def explain_topic(topic: str) -> str:
    """
    Generate an educational explanation for the given topic.
    """

    try:
        # Validate topic
        if not topic or not topic.strip():
            return "Please enter a topic to explain."

        topic = topic.strip()

        # Get explanation mode safely
        mode = str(EXPLANATION_MODE).strip().lower()

        # Local AI model
        if mode == "local":
            return _local_explain(topic)

        # Gemini AI
        prompt = f"""
Explain the following educational topic for a beginner.

Topic:
{topic}

Use this structure:

1. Simple definition
2. How it works / main idea
3. Three key points
4. One simple example
5. One-line recap

Use easy English.
Avoid unnecessary technical jargon.
Make the explanation clear and suitable for a college student.
"""

        response = generate_text(
            prompt,
            system_instruction=(
                "You are EduGenie, a patient tutor "
                "who simplifies difficult concepts "
                "using clear and easy English."
            )
        )

        if not response:
            return "Sorry, I could not generate an explanation."

        return response.strip()

    except Exception as exc:
        return user_friendly_error(exc)