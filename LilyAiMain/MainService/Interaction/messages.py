"""Platform-agnostic message types shared by Discord, the API and the DM Simulator."""
from dataclasses import dataclass, field
from typing import Any


@dataclass
class ImageAttachment:
    """An image the user sent along with a message (e.g. a game screenshot). Held in memory only."""
    data: bytes
    mime: str = "image/png"
    name: str = "image"


@dataclass
class IncomingMessage:
    user_id: str
    text: str
    display_name: str = ""
    source: str = "discord"  # discord | simulator | web
    images: list[ImageAttachment] = field(default_factory=list)


@dataclass
class MenuItem:
    label: str
    text: str  # message sent on the user's behalf when picked


@dataclass
class OutgoingMessage:
    text: str
    kind: str = "chat"  # chat | system
    reply_id: str = ""
    menu: list[MenuItem] = field(default_factory=list)
    meta: dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict:
        return {
            "text": self.text, "kind": self.kind, "reply_id": self.reply_id,
            "menu": [{"label": m.label, "text": m.text} for m in self.menu], "meta": self.meta,
        }
