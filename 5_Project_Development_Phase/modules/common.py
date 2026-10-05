def user_friendly_error(
    exc: Exception
) -> str:

    message = str(
        exc
    ).strip()

    if not message:

        message = (
            "An unexpected error occurred."
        )

    return (
        "EduGenie could not complete "
        "the request: "
        + message
    )