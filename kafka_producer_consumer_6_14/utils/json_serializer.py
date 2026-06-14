import json

def serialize_message(message: dict) -> bytes:
    return json.dumps(message).encode("utf-8")


def deserialize_message(message_bytes: bytes) -> dict:
    return json.loads(message_bytes.decode("utf-8"))