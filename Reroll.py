
from Tossing import Toss

class Reroll:

    def __init__(self):
        pass

    @staticmethod
    def pickDice(outcome,count = 0):
        print("Which of these dice do you want to reroll? Pick numbers separated by comas.")
        print(outcome)
        result = []

        while True:
            pick = input()
            result = [x.strip() for x in pick.split(',')]

            for die in result:
                if int(die) not in outcome:
                    print("You don't have this record in your dice pool, try again")
                    continue
                else:
                    count += 1
                    outcome.remove(int(die))
            break

        Toss.d6(dice=count, value=outcome)



