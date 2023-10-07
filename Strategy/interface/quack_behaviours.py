from typing import Protocol

class QuackBehaviour(Protocol):
    def quack(self):
        raise NotImplementedError()