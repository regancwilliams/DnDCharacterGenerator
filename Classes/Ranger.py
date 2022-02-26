from Constants import EquiptmentPacks
from random import randint
import random
from Subclasses import RangerSubclasses
from Weapons import Weapons
from Character import Character

class RangerDetails(Character):

    def __init__(self):
        self.height = 1
        self.age = 1

    def getRangerEquiptment(self):
        equiptment = []
        weapon = Weapons()

        if (randint(0,1) == 0):
            equiptment.append("Scale Mail")
        else:
            equiptment.append("Leather Armor")

        if (randint(0,1) == 0):
            equiptment.append("2 Shortswords")
        else:
            equiptment.append(weapon.getSimpleMeleeWeapon())
            equiptment.append(weapon.getSimpleMeleeWeapon())

        if (randint(0,1) == 0):
            equiptment.append(EquiptmentPacks.DUNGEONEERS_PACK)
        else:
            equiptment.append(EquiptmentPacks.EXPLORERS_PACK)

        equiptment.append("Longbow and a quiver of 20 arrows")

        self.equiptment = equiptment

    def getRangerSubclass(self):
        return random.choice(list(RangerSubclasses))
