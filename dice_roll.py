import random


class Dice:
    def roll():
        value1 = random.randint(1, 6)
        value2 = random.randint(1, 6)
        return value1, value2


dice = Dice()
print(dice.roll())
