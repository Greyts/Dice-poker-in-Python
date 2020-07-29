# Comparing two outcomes and determining who wins
from Tossing import Toss

class Comparing:


    def __init__(self, hand):
        self.hand = hand
        pass

    @staticmethod
    def handValue(hand):
        value = 0

        for n in range (1,7):

            if ('four' +str(n)) in hand:
                value += (8 + n/10)

            if ('pair' + str(n)) in hand:
                hand.remove('pair' + str(n))
                value += (1 + n/10)

            elif ('three' + str(n)) in hand:
                value += (4 + n/10)

        if 'straight' in hand:
            value += 5

        if 'bigger_straight' in hand:
            value += 6

        if 'full house' in hand:
            value += 7

        if 'flush' in hand:
            value += 9

        print(value)
        return value

    @staticmethod
    def comparison(hand_1,hand_2):
        if hand_1 > hand_2:
            print("Player wins!!!")
        elif hand_1 == hand_2:
            print("It's a draw!!!")
        else:
            print('Bot wins!')