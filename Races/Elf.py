from Character import Character
from random import randint
from RaceConstants import *

class ElfDetails(Character):

    # Elves range from under 5 to over 6 feet tall
    def getHeight(self):
        return randint(Height.ELF_MIN_HEIGHT.value, Height.ELF_MAX_HEIGHT.value)

    # Although elves reach physical maturity at about the same age as humans,
    # the elven understanding of adulthood goes beyone physicl growth to
    # encompass wordly experince. An elf typically claims adulthood and an
    # adult name around the age of 100 and can live to be 750 years old
    def getAge(self):
        return randint(Age.ELF_MIN_AGE.value, Age.ELF_MAX_AGE.value)

    # Your base walking speed is 30 feet
    def getSpeed(self):
        return Speed.ELF_SPEED.value

    # Elves have slender builds
    def getWeight(self):
        return randint(Weight.ELF_MIN_WEIGHT.value, Weight.ELF_MAX_WEIGHT.value)
