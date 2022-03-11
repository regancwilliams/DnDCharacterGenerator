from Character import Character
from random import randint
import random
from Subclasses import SorcererSubclasses
from Weapons import Weapons

class SorcererDetails(Character):

    def getEquiptment(self):

        # Array to hold all rogue equiptment
        equiptment = []
        weapon = Weapons()

        num = randint(0, 1)
        if num == 0:
            equiptment.append("A light crossbow and 20 bolts")
        else:
            equiptment.append(weapon.getSimpleWeapon())

        num = randint(0, 1)
        if num == 0:
            equiptment.append("A component pouch")
        elif num == 1:
            equiptment.append("An arcane focus")

        num = randint(0, 1)
        if num == 0:
            equiptment.append("A component pouch")
        elif num == 1:
            equiptment.append("An arcane focus")

        equiptment.append("2 daggers")

        self.equiptment = equiptment

    def getSubclass(self):
        return random.choice(list(SorcererSubclasses))
