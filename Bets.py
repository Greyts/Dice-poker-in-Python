from Tossing import Toss

class Bets:

    def __init__(self, wallet = 50):
        self.wallet = wallet

    def bets(self):

        while True:
            if self.wallet == 0:
                print("Your wallet is empty!")
            else:
                print("Your ballance is {} $.".format(self.wallet))
                print("Place you bets.")
                bet = int(input())
                try:
                    bet is int
                except ValueError:
                    print("Your bet has to be integer and has to be lower, or equal to your account balance")
                    continue

                if bet > self.wallet:
                    print("You balance is lower than desired bet!")
                    continue
                else:

                    self.wallet -= bet



        return bet