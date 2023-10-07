from Strategy import Duck


class SaxonDuck(Duck):
    def __init__(self):
        super(Duck, self).__init__()
        self.fly_behaviour = FlyNoWay()
        self.quack_behaviour = Quack()
    
    def display(self):
        print("Я саксонская утка")