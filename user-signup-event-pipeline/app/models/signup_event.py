import json


class SignupEvent:

    REQUIRED_FIELDS = [
        "user_id",
        "name",
        "email"
    ]

    @classmethod
    def validate(cls, event_data):

        missing_fields = [
            field
            for field in cls.REQUIRED_FIELDS
            if field not in event_data
        ]

        if missing_fields:
            raise ValueError(
                f"Missing fields: {missing_fields}"
            )

        return True

    @classmethod
    def to_json(cls, event_data):

        cls.validate(event_data)

        return json.dumps(event_data)

    @classmethod
    def from_json(cls, json_string):

        event_data = json.loads(json_string)

        cls.validate(event_data)

        return event_data