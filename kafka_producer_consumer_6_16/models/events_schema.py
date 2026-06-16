REQUIRED_FIELDS = [
    "event_type",
    "user_id",
    "timestamp"
]


def validate_event(event):

    for field in REQUIRED_FIELDS:

        if field not in event:
            raise ValueError(
                f"Missing required field: {field}"
            )

    return True