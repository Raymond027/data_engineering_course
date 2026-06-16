import random
from src.schemas.events import (
    create_user_signup,
    create_user_login,
    create_order_created
)

def generate_event():
    event_type = random.choice([
        "signup",
        "login",
        "order"
    ])

    if event_type == "signup":
        return create_user_signup("user_1")

    if event_type == "login":
        return create_user_login("user_1")

    return create_order_created("user_1", "order_123")