from random import randint
import math

class AbilityScores():

    # TODO: Add different ways to get the score
    # Calcualte the ability score by rolling 4d6 and rerolling the lowest number
    def getRandomScore(self):
        diceRolls = []
        for dice in range(4):
            diceRolls.append(randint(1,6))

        # Remove the lowest roll
        lowestRoll = min(diceRolls)
        diceRolls.remove(lowestRoll)

        # Replace the lowest roll
        diceRolls.append(randint(1,6))

        return sum(diceRolls)

    def getAbilityModifier(self, abilityScore):
        return math.floor((abilityScore - 10) / 2)
