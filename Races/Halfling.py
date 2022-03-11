from Character import Character
from random import randint
from RaceConstants import *

class HalflingDetails(Character):

    # Halflings average about 3 feet tall
    def getHeight(self):
        return randint(Height.HALFLING_MIN_HEIGHT.value, Height.HALFLING_MAX_HEIGHT.value)

    # A halfling reaches adulthood at the age of 20 and generally lives into
    # the middle of their second century
    def getAge(self):
        return randint(Age.HALFLING_MIN_AGE.value, Age.HALFLING_MAX_AGE.value)

    # Your base walking speed is 25 feet
    def getSpeed(self):
        return Speed.HALFLING_SPEED.value

    # Halflings avearag about 40 pounds
    def getWeight(self):
        return randint(Weight.HALFLING_MIN_WEIGHT.value, Weight.HALFLING_MAX_WEIGHT.value)

    def updateAbilityScore(self, halfling):
        halfling.dexterity += 2
