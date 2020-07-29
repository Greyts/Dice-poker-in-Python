# Dice tossing module

import random
class Toss:


    def __init__(self, dice = 5 , sides = 6, value = [], name = ''):
        self.dice = dice
        self.sides = sides
        self.value = value
        self.name = name

    def __name__(self,name):
        return name

    def __str__(self):
        return ("You've tossed {} {}-sided dice!".format(self.dice,self.sides))

    def tossing(self, dice = 5, sides = 6, value = None):


        self.value = []
        while self.dice >= 1:
            self.value.append(random.randint(1,self.sides))
            self.dice -= 1

        self.dice = dice
        return self.value

    @staticmethod
    def d6(dice = 0, sides = 6, value = 0):

        while dice >= 1:
            value.append(random.randint(1,sides))
            dice -= 1
        print(value)
        return value