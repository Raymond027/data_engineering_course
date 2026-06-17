from app.utils.logger import logger


def send_welcome_email(user):

    print(
        f"Welcome email sent to "
        f"{user['name']} "
        f"({user['email']})"
    )

    logger.info(
        f"Welcome email processed for "
        f"{user['email']}"
    )