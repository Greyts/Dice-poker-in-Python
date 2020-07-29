# To do list
# Dice tossing module

from Tossing import Toss
from Figures import Figure
from Comparing import Comparing
from Reroll import Reroll

player = Toss(name='player')
bot = Toss(name='bot')

outcome_1 = player.tossing()
outcome_2 = bot.tossing()

# Detecting figures

print(outcome_1, player)
print(outcome_2, bot)

hand_1 = Figure.checking(outcome_1)
hand_2 = Figure.checking(outcome_2)

# Comparing two outcomes and determining who wins

player_value = Comparing.handValue(hand_1)
bot_value = Comparing.handValue(hand_2)

Comparing.comparison(player_value, bot_value)


# Module to let both players and bot to decide whether they want to toss particular dice


while True:
    reroll = input(str("Do you want to reroll any of the dice? y/n?   "))
    if reroll == 'y':
        break
    elif reroll == 'n':
        print("Any change of plans?")
    else:
        print("Input has to be either y or n!")

Reroll.pickDice(outcome_1)
hand_1 = Figure.checking(outcome_1)
player_value = Comparing.handValue(hand_1)
Comparing.comparison(player_value, bot_value)


# Betting/winning/losing module

