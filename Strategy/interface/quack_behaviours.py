@Abstract
class QuackBehaviour:
    def quack(self):
        raise NotImplementedError()

class QuackLoud(QuackBehaviour):
    def quack(self):
        print("Я крякаю громко")

class QuackLong(QuackBehaviour):
    def quack(self):
        print("Я крякаю протяжно")

class QuackNoQuack(QuackBehaviour):
    def quack(self):
        print("Я не умею крякать")

class QuackRarely(QuackBehaviour):
    def quack(self):
        print("Я крякаю редко")