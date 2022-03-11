from Character import Character
from random import randint
from RaceConstants import *

class DwarfDetails(Character):

    # Dwarves stand between 4 and 5 feet tall
    def getHeight(self):
        return randint(Height.DWARF_MIN_HEIGHT.value, Height.DWARF_MAX_HEIGHT.value)

    # Dwarves matture at the same rate as humans, but they're considred young
    # until they reach the age of 50. On average, they live about 350 years.
    def getAge(self):
        return randint(Age.DWARF_MIN_AGE.value, Age.DWARF_MAX_AGE.value)

    # Your base walking speed is 25 feet. Your speed is not reduced by wearing
    # heavy armor.
    def getSpeed(self):
        return Speed.DWARF_SPEED.value

    # Dwarves average about 150 pounds
    def getWeight(self):
        return randint(Weight.DWARF_MIN_WEIGHT.value, Weight.DWARF_MAX_WEIGHT.value)

    def updateAbilityScore(self, dwarf):
        dwarf.constitution += 2
