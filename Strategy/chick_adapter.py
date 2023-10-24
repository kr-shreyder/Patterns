from duck import Duck
from interface.chicken import Chicken

class ChickenAdapter(Duck):
    def __init__(
        self,
        chicken: Chicken
    ):
        self.chicken = chicken

    def perform_fly(self):
        Chicken.fly()
        Chicken.fly()
        Chicken.fly()
    
    def perform_quack(self):
        Chicken.clack()

    def display():
        ...