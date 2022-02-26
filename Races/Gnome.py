from Character import Character
from random import randint
from RaceConstants import *

class GnomeDetails(Character):

    # Gnomes are between 3 and 4 feet tall
    def getHeight(self):
        return randint(Height.GNOME_MIN_HEIGHT.value, Height.GNOME_MAX_HEIGHT.value)

    # Gnomes mature at the same rate humans do, and most are expected to settle
    # down into an adult life by around age 40. They can live up to 500 years
    def getAge(self):
        return randint(Age.GNOME_MIN_AGE.value, Age.GNOME_MAX_AGE.value)

    # Your base walking speed is 25 feet
    def getSpeed(self):
        return Speed.GNOME_SPEED.value

    # Gnomes avearag about 40 pounds
    def getWeight(self):
        return randint(Weight.GNOME_MIN_WEIGHT.value, Weight.GNOME_MAX_WEIGHT.value)
