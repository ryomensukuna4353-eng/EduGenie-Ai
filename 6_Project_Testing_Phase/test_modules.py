from unittest.mock import patch

from modules.qna import answer_question
from modules.summary import summarize_text


def test_qna_uses_gemini():

    with patch(
        "modules.qna.generate_text",
        return_value="Test answer"
    ):

        result = answer_question(
            "What is Python?"
        )

        assert result == "Test answer"


def test_summary_uses_gemini():

    with patch(
        "modules.summary.generate_text",
        return_value="Short summary"
    ):

        result = summarize_text(
            "Long educational text"
        )

        assert result == "Short summary"