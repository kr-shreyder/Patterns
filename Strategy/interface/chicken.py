from typing import Protocol

class Chicken(Protocol):
    def fly(self):
        raise NotImplementedError()
    
    def clack(self):
        raise NotImplementedError()