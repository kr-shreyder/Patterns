from typing import Protocol

class FlyBehaviour(Protocol):
    def fly(self):
        raise NotImplementedError()