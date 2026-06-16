from dataclasses import dataclass
from typing import Literal, Dict, Any
import time

EventType = Literal["user_signup", "user_login", "order_created"]

@dataclass
class BaseEvent:
    event_type: EventType
    user_id: str
    timestamp: int

    def to_dict(self) -> Dict[str, Any]:
        return self.__dict__


def create_user_signup(user_id: str) -> dict:
    return {
        "event_type": "user_signup",
        "user_id": user_id,
        "timestamp": int(time.time()),
        "email": f"{user_id}@example.com"
    }


def create_user_login(user_id: str) -> dict:
    return {
        "event_type": "user_login",
        "user_id": user_id,
        "timestamp": int(time.time()),
        "device": "web"
    }


def create_order_created(user_id: str, order_id: str) -> dict:
    return {
        "event_type": "order_created",
        "user_id": user_id,
        "order_id": order_id,
        "amount": 99.99,
        "currency": "USD",
        "timestamp": int(time.time())
    }