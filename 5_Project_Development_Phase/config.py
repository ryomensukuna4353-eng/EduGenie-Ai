import os

from dotenv import load_dotenv


# Load .env
load_dotenv()


APP_NAME = os.getenv(
    "APP_NAME",
    "EduGenie"
)


GEMINI_API_KEY = os.getenv(
    "GEMINI_API_KEY",
    ""
).strip()


GEMINI_MODEL = os.getenv(
    "GEMINI_MODEL",
    "gemini-2.5-flash"
).strip()


EXPLANATION_MODE = os.getenv(
    "EXPLANATION_MODE",
    "gemini"
).strip().lower()


LOCAL_EXPLANATION_MODEL = os.getenv(
    "LOCAL_EXPLANATION_MODEL",
    "MBZUAI/LaMini-Flan-T5-783M"
).strip()


MAX_INPUT_CHARS = int(
    os.getenv(
        "MAX_INPUT_CHARS",
        "12000"
    )
)


MAX_OUTPUT_TOKENS = int(
    os.getenv(
        "MAX_OUTPUT_TOKENS",
        "1200"
    )
)


TEMPERATURE = float(
    os.getenv(
        "TEMPERATURE",
        "0.4"
    )
)