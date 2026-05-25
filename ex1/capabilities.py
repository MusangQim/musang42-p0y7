from abc import ABC, abstractmethod


class HealCapability(ABC):
    @abstractmethod
    def heals(self) -> str:
        pass


class TransformCapability(ABC):
    def __init__(self, transform: bool) -> None:
        self.transformed = False

    @abstractmethod
    def transform(self) -> str:
        pass

    @abstractmethod
    def revert(self) -> str:
        pass
