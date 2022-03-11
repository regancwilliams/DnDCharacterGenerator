from Character import Character
from random import randint
from RaceConstants import *

class HalfElfDetails(Character):

    # Half-elfves are about the same size as humans ranging from 5
    # to 6 feet tall
    def getHeight(self):
        return randint(Height.HALFELF_MIN_HEIGHT.value, Height.HALFELF_MAX_HEIGHT.value)

    # Half-elves mature at the same rate humans do and reach adulthood around
    # the age of 20. They live much longer than humans, however, often
    # exceeding 180 years
    def getAge(self):
        return randint(Age.HALFELF_MIN_AGE.value, Age.HALFELF_MAX_AGE.value)

    # Your base walking speed is 30 feet
    def getSpeed(self):
        return Speed.HALFELF_SPEED.value

    # Halfelves are about the same size as humans
    def getWeight(self):
        return randint(Weight.HALFELF_MIN_WEIGHT.value, Weight.HALFELF_MAX_WEIGHT.value)

    def updateAbilityScore(self, halfElf):
        halfElf.charisma += 2
        #TODO: Increase 2 other ability scores of your choice by 1
