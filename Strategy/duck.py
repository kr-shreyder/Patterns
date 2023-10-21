from interface import FlyBehaviour, QuackBehaviour
from abc import ABC

class Duck(ABC):
    def __init__(
        self,
        fly_behavior: FlyBehaviour,
        quack_behavior: QuackBehaviour,
        name: str
    ): 
        self.name = name
        self._fly_behavior = fly_behavior
        self._quack_behavior = quack_behavior

    def perform_fly(self):
        self._fly_behavior.fly()

    def perform_quack(self):
        self._quack_behavior.quack()

    def set_fly_behavior(self, fly_behavior: FlyBehaviour):
        self._fly_behavior = fly_behavior

    def set_quack_behavior(self, quack_behavior: QuackBehaviour):
        self._quack_behavior = quack_behavior

    def display(self):
        print(self.name)
        self.perform_fly()
        self.perform_quack()

class DuckExtnd(Duck):
    ...