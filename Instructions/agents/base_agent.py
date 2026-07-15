from abc import ABC, abstractmethod

# gibt Struktur vor, die alle Agents implementieren müssen
class BaseAgent(ABC):

    @abstractmethod
    def execute(self, intake):
        pass