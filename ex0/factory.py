from abc import ABC, abstractmethod


class CreatureFactory(ABC):
    def __init__(self):
    def create_base():
    def create_evolved():


class FlameFactory(CreatureFactory):
    def create_base():
        return Flameling()
    def create_evolved():
        return Pyrodon()


class AquaFactory(CreatureFactory):
    def create_base():
        return Aquabub()
    def create_evolved():
        return Torragon()