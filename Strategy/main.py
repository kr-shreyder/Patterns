from behaviours.fly import FlyOnWings, FlyNoFly
from behaviours.quack import QuackNoQuack, QuackRarely
from duck import Duck

fly_on_wings = FlyOnWings()
fly_no_fly = FlyNoFly()
quack_mute = QuackNoQuack()
quack_rare = QuackRarely()

saxon_duck = Duck(
    name="Саксонская утка",
    fly_behavior=fly_on_wings,
    quack_behavior=quack_rare
)
rubber_duck = Duck(
    name="Резиновая утка",
    fly_behavior=fly_no_fly,
    quack_behavior=quack_mute
)

ducks = [
    saxon_duck,
    rubber_duck,
]

for duck in ducks:
    duck.display()
    print()
