from Tossing import Toss
from Bets import Bets
from Figures import Figure
from Comparing import Comparing
from Reroll import Reroll

class Profile(Toss, Bets, Figure, Comparing, Reroll):

    def __init__(self, name = '', wallet = 50, hand = []):

        self.hand = hand
        self.name = name
        self.wallet = wallet


    def __str__(self):
        return("Name is {}, ballance is {}, hand is {}. ". format(self.name,self.wallet,self.hand))