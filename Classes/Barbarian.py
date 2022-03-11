from random import randint
import random
from Subclasses import BarbarianSubclasses
from Character import Character
from Weapons import Weapons

class BarbarianDetails(Character):

    def getEquiptment(self):
        equiptment = []
        weapon = Weapons()

        num = randint(0, 1)
        if num == 0:
            equiptment.append("Greataxe")
        else:
            equiptment.append(weapon.getMartialMeleeWeapon())

        num = randint(0, 1)
        if num == 0:
            equiptment.append("2 handaxes")
        else:
            equiptment.append(weapon.getSimpleWeapon())

        equiptment.append("Explorers Pack")
        equiptment.append("4 Javelins")

        self.equiptment = equiptment

    def getSubclass(self):
        return random.choice(list(BarbarianSubclasses))
