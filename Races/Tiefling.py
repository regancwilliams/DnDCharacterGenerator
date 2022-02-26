from Character import Character
from random import randint
from RaceConstants import *

class TieflingDetails(Character):

    def getHeight(self):
        return 2

    def getAge(self):
        return randint(12, 100)

    def getSpeed(self):
        return Speed.TIEFLING_SPEED
