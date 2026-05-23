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

    def attack(self):
        return ("Flameling uses Ember!")


class Pyrodon(Creature):
    def __init__(self, name="Pyrodon", type="Fire/Flying") -> None:
        super().__init__(name, type)

    def attack(self) -> str:
        return ("Pyrodon uses Flamethrower!")


class Aquabub(Creature):
    def __init__(self, name="Aquahub", type="Water") -> None:
        super().__init__(name, type)

    def attack(self) -> str:
        return ("Aquabub uses Water Gun!")


class Torragon(Creature):
    def __init__(self, name="Torragon", type="Water") -> None:
        super().__init__(name, type)

    def attack(self) -> str:
        return ("Torragon uses Hydro Pump!")
