from abc import ABC


class Baverage(ABC):
    def __init__(self, price: float, description: str):
        self.price = price
        self.description = description

    def cost(self) -> float:
        return self.price

    def get_description(self) -> str:
        return self.description
    

class FlavoringDecorator(Baverage):
    def __init__(self, baverage: Baverage, price: float, description: str):
        self.baverage = baverage
        super().__init__(price, description)

    def cost(self) -> float:
        return self.baverage.cost() + self.price
    
    def get_description(self) -> str:
        return f"{self.baverage.get_description()} + {self.description}"
    

class Raf(Baverage):
    def __init__(self, price: float, description: str):
        super().__init__(price, description)


class Latte(Baverage):
    def __init__(self, price: float, description: str):
        super().__init__(price, description)


class Espresso(Baverage):
    def __init__(self, price: float, description: str):
        super().__init__(price, description)


class Milk(FlavoringDecorator):
    def __init__(self, baverage: Baverage, price: float, description: str,):
        super().__init__(baverage, price, description)


class Choco(FlavoringDecorator):
    def __init__(self, baverage: Baverage, price: float, description: str):
        super().__init__(baverage, price, description)


baverage = Latte(price=100, description="Большой латте")
baverage = Milk(baverage=baverage, price=100, description="Молоко")
baverage = Milk(baverage=baverage, price=100, description="Молоко")
baverage = Choco(baverage=baverage, price=100, description="Шоколад")
print(baverage.get_description())
print(baverage.cost())