from abc import ABC, abstractmethod


class AbstractEntity(ABC):
    """Абстрактный класс для классов с общими свойствами"""

    @abstractmethod
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description

    @abstractmethod
    def __str__(self) -> str:
        pass
