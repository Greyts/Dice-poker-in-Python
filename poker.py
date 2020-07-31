# To do list
# Dice tossing module

from Tossing import Toss
from Figures import Figure
from Comparing import Comparing
from Reroll import Reroll
from Bets import Bets
from Profile import Profile

#Creating player's and bot's profiles

player = Profile(name='player')
bot = Profile(name='bot')
print(player)

#Dice tossing

outcome_1 = player.tossing()
outcome_2 = bot.tossing()

player.hand = outcome_1
bot.hand = outcome_2

# Detecting figures

print(outcome_1, player)
print(outcome_2, bot)

hand_1 = player.checking(outcome_1)
hand_2 = bot.checking(outcome_2)

# Comparing two outcomes and determining who wins

player_value = player.handValue(hand_1)
bot_value = bot.handValue(hand_2)

Comparing.comparison(player_value, bot_value)


# Module to let both player and bot to decide whether they want to reroll particular dice


while True:
    reroll = input(str("Do you want to reroll any of the dice? y/n?   "))
    if reroll == 'y':
        player.pickDice(outcome_1)
        hand_1 = Figure.checking(outcome_1)
        player_value = player.handValue(hand_1)
        Comparing.comparison(player_value, bot_value)
        break

    elif reroll == 'n':
        break

    else:
        print("Input has to be either y or n!")



player.bets()


# Betting/winning/losing module

