from dataclasses import dataclass


@dataclass
class AgentResult:

    success: bool

    category: str

    message: str