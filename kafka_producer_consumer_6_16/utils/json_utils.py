import json

from utils.logger import logger


def serialize_event(event):

    try:
        return json.dumps(event)

    except Exception as error:
        logger.error(f"JSON serialization failed: {error}")
        raise


def deserialize_event(message):

    try:
        return json.loads(message)

    except json.JSONDecodeError as error:

        logger.error(
            f"Invalid JSON received: {error}"
        )

        return None

    except Exception as error:

        logger.error(
            f"Unexpected JSON error: {error}"
        )

        return None