import time

from utils.logger import logger


def retry_operation(operation, retries, delay):
    """
    Retry operation multiple times.
    """

    for attempt in range(1, retries + 1):
        try:
            return operation()

        except Exception as error:

            logger.error(
                f"Attempt {attempt}/{retries} failed: {error}"
            )

            if attempt < retries:
                time.sleep(delay)

    raise Exception("Maximum retry attempts exceeded.")