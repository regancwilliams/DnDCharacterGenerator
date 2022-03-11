from Character import Character
from random import randint
from RaceConstants import *

class DragonbornDetails(Character):

    # Dragonborn are taller the humans, standing well over 6 feet tall
    def getHeight(self):
        return randint(Height.DRAGONBORN_MIN_HEIGHT.value, Height.DRAGONBORN_MAX_HEIGHT.value)

    # Young dragonborn grow quickly. They walk hours after hatching, attain the
    # side and development of a 10-year-old human child by the age of 3, and
    # reach adulthood by 15. They live to be around 80
    def getAge(self):
        return randint(Age.DRAGONBORN_MIN_AGE.value, Age.DRAGONBORN_MAX_AGE.value)

    # Your base walking speed is 30 feet
    def getSpeed(self):
        return Speed.DRAGONBORN_SPEED.value

    # Dragonborn are heavier than humans, averaging almost 250 pounds
    def getWeight(self):
        return randint(Weight.DRAGONBORN_MIN_WEIGHT.value, Weight.DRAGONBORN_MAX_WEIGHT.value)

    def updateAbilityScore(self, dragonborn):
        dragonborn.strength += 2
        dragonborn.charisma += 1
