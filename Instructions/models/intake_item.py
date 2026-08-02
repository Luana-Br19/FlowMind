from dataclasses import dataclass, field
from typing import List, Dict


@dataclass
class IntakeItem:
    text: str
    input_type: str
    tags: List[str] = field(default_factory=list)
    attachments: str = ""  #List[str] = field(default_factory=list)
    
    id: str = ""
    user: str = ""
    source: str = "Slack"
    channel: str = ""
    category: str = ""

    metadata: Dict = field(default_factory=dict)

