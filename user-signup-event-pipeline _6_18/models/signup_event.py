from dataclasses import dataclass


@dataclass
class SignupEvent:
    user_id: int
    username: str
    email: str

    def to_dict(self):
        return {
            "user_id": self.user_id,
            "username": self.username,
            "email": self.email
        }