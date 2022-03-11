from Character import Character
from random import randint
import random
from Subclasses import PaladinSubclasses
from Weapons import Weapons

class PaladinDetails(Character):

    def getPaladinEquiptment(self):
        equiptment = []
        weapon = Weapons()

        if (randint(0,1) == 0):
            equiptment.append(weapon.getMartialWeapon())
            equiptment.append("Shield")
        else:
            equiptment.append(weapon.getMartialWeapon())
            equiptment.append(weapon.getMartialWeapon())

        if (randint(0,1) == 0):
            equiptment.append("5 Javelines")
        else:
            equiptment.append(weapon.getSimpleMeleeWeapon())

        if (randint(0,1) == 0):
            equiptment.append("Priest's Pack")
        else:
            equiptment.append("Explorer's Pack")

        equiptment.append("Chain Mail")
        equiptment.append("Holy Symbol")

        self.equiptment = equiptment

    def getPaladinSubclass(self):
        return random.choice(list(PaladinSubclasses))
