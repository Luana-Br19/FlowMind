from dataclasses import dataclass, field
from typing import List, Dict


@dataclass
class IntakeItem:
    text: str
    tags: List[str] = field(default_factory=list)
    attachments: List[str] = field(default_factory=list)

    source: str = "Slack"
    channel: str = ""
    user: str = ""

    metadata: Dict = field(default_factory=dict)