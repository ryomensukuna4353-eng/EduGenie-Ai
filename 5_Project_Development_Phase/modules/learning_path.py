from gemini_client import generate_text

from modules.common import (
    user_friendly_error
)


def get_learning_recommendations(
    topic: str
) -> str:

    prompt = f"""
Create a personalized learning path
for the topic below.

Topic:

{topic}

Include:

1. Beginner prerequisites

2. Beginner concepts

3. Intermediate concepts

4. Advanced concepts

5. Suggested 4-week timeline

6. Practice activities

7. Revision strategy

8. Useful resource types
   such as official documentation,
   textbooks, practice websites,
   and educational videos.

9. A checklist showing when
   the learner is ready to move
   to the next level.

Make the plan practical
and student-friendly.

Do not invent specific URLs.
"""


    try:

        return generate_text(

            prompt,

            system_instruction=(
                "You are an educational mentor "
                "who creates structured and practical "
                "learning plans."
            )
        )

    except Exception as exc:

        return user_friendly_error(
            exc
        )