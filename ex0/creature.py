from abc import ABC, abstractmethod


class Creature(ABC):
    def __init__(self, name: str, type: str):
        self.name = name
        self.type = type

    @abstractmethod
    def attack(self) -> str:
        pass

    def describe(self) -> str:
        return (f"{self.name} is a {self.type} type Creature")


class Flameling(Creature):
    def __init__(self, name="Flameling", type="Fire") -> None:
        super().__init__(name, type)


class Pyrodon(Creature):
    def __init__(self, name="Pyrodon", type="Fire/Flying") -> None:
        super().__init__(name, type)


class Aquahub(Creature):
    def __init__(self, name="Aquahub", type="Water") -> None:
        super().__init__(name, type)


class Torragon(Creature):
    def __init__(self, name="Torragon", type="Water") -> None:
        super().__init__(name, type)
