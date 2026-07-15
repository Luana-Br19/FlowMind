from dataclasses import dataclass, field
from typing import List

# später von Claude, nur Dummy
@dataclass
class Plan:

    category: str

    tasks: List[str] = field(default_factory=list)