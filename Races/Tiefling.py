from Character import Character
from random import randint
from RaceConstants import *

class TieflingDetails(Character):

    def getHeight(self):
        return 2

    def getAge(self):
        return randint(12, 100)

    def getSpeed(self):
        return Speed.TIEFLING_SPEED.value

    def getWeight(self):
        return randint(Weight.TIEFLING_MIN_WEIGHT.value, Weight.TIEFLING_MAX_WEIGHT.value)

    def updateAbilityScore(self, tiefling):
        tiefling.intelligence += 1
        tiefling.charisma += 2
