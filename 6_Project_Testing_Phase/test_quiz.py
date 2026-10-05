from unittest.mock import patch

from modules.quiz import generate_quiz


def test_quiz_parsing():

    fake_json = """
    {
        "questions": [

            {
                "question": "2 + 2 = ?",
                "options": [
                    "1",
                    "2",
                    "3",
                    "4"
                ],
                "correct_answer": "4",
                "explanation": "Two plus two equals four."
            },

            {
                "question": "Capital of France?",
                "options": [
                    "Paris",
                    "Rome",
                    "Berlin",
                    "Madrid"
                ],
                "correct_answer": "Paris",
                "explanation": "Paris is the capital of France."
            },

            {
                "question": "Water formula?",
                "options": [
                    "CO2",
                    "H2O",
                    "O2",
                    "NaCl"
                ],
                "correct_answer": "H2O",
                "explanation": "Water is H2O."
            }

        ]
    }
    """


    with patch(
        "modules.quiz.generate_structured",
        return_value=fake_json
    ):

        result = generate_quiz(
            "Simple test content"
        )


    assert len(
        result["questions"]
    ) == 3


    assert all(
        len(question["options"]) == 4
        for question in result["questions"]
    )