from dataclasses import dataclass
from typing import Dict, List

@dataclass
class AgentResult:

    success: bool

    category: str

    folder: str

    filename: str

    title: str

    tags: List[str]

    #content: Dict

