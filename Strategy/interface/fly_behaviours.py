@Abstract
class FlyBehaviour:
    def fly(self):
        raise NotImplementedError()


class FlyOnWings(FlyBehaviour):
    def fly(self):
        print("Я летаю на крыльях!")


class FlyNoFLy(FlyBehaviour):
    def fly(self):
        print("Я не умею летать")


class FlyRocket(FlyBehaviour):
    def fly(self):
        print("Я летаю на ракете")
        
class FlyThrow(FlyBehaviour):
    def fly(self):
        print("Я летаю на радиоуправлении")