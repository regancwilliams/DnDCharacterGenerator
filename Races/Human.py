from Character import Character
from random import randint
from RaceConstants import *

class HumanDetails(Character):

    # Humans vary widly in height and build, from barely 5 feet to well over
    # 6 feet tall
    def getHeight(self):
        return randint(Height.HUMAN_MIN_HEIGHT.value, Height.HUMAN_MAX_HEIGHT.value)

    # Humans reach adulthood in thier late teens and live less than a centry
    def getAge(self):
        return randint(Age.HUMAN_MIN_AGE.value, Age.HUMAN_MAX_AGE.value)

    # Your base walking speed is 30 feet
    def getSpeed(self):
        return Speed.HUMAN_SPEED.value

    def getWeight(self):
        return randint(Weight.HUMAN_MIN_WEIGHT.value, Weight.HUMAN_MAX_WEIGHT.value)

    def updateAbilityScore(self, human):
        human.charisma += 1
        human.constitution += 1
        human.dexterity += 1
        human.intelligence += 1
        human.strength += 1
        human.wisdom += 1
