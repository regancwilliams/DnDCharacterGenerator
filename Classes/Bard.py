from random import randint
import random
from Subclasses import BardSubclasses
from Character import Character
from Weapons import Weapons

class BardDetails(Character):

    def getEquiptment(self):
        equiptment = []
        weapon = Weapons()

        num = randint(0, 2)
        if num == 0:
            equiptment.append("Rapier")
        elif num == 1:
            equiptment.append("Longsword")
        else:
             equiptment.append(weapon.getSimpleWeapon())

        num = randint(0, 1)
        if num == 0:
            equiptment.append("Diplomat's pack")
        else:
            equiptment.append("Entertainer's pack")

        equiptment.append(weapon.getMusicalInstrument())
        equiptment.append("Leather armor")
        equiptment.append("1 dagger")

        self.equiptment = equiptment

    def getSubclass(self):
        return random.choice(list(BardSubclasses))
