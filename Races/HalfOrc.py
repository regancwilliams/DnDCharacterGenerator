from Character import Character
from random import randint
from RaceConstants import *

class HalfOrcDetails(Character):

    # Half-orcs range from 5 to well over 6 feet tall
    def getHeight(self):
        return randint(Height.HALFORC_MIN_HEIGHT.value, Height.HALFORC_MAX_HEIGHT.value)

    # Half-orcs mature a little faster than humans, reaching adulthood around
    # age 14. They age noticeably faster and rarely live longer than 75 years
    def getAge(self):
        return randint(Age.HALFORC_MIN_AGE.value, Age.HALFORC_MAX_AGE.value)

    # Your base walking speed is 30 feet
    def getSpeed(self):
        return Speed.HALFORC_SPEED.value

    # Halforcs are somewhat larger and bulkier than humans
    def getWeight(self):
        return randint(Weight.HALFORC_MIN_WEIGHT.value, Weight.HALFORC_MAX_WEIGHT.value)

    def updateAbilityScore(self, halfOrc):
        halfOrc.constitution += 1
        halfOrc.strength += 2
