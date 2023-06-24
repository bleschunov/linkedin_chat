from dataclasses import dataclass


@dataclass
class Message:
    text: str
    is_me: bool
    avatar: str
