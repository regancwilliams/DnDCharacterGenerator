from random import randint
import random
from Subclasses import BarbarianSubclasses
from Character import Character

class BarbarianDetails(Character):

    def __init__(self):
        self.height = 1
        self.age = 1

    def getBarbarianEquiptment(self, simpleMeleeWeapons, simpleRangedWeapons, martialMeleeWeapons):
        equiptment = []
        num = randint(0, 1)
        if num == 0:
            equiptment.append("Greataxe")
        else:
            equiptment.append(martialMeleeWeapons[randint(0, len(martialMeleeWeapons) - 1)])
        num = randint(0, 1)
        if num == 0:
            equiptment.append("2 handaxes")
        else:
            simpleWeaponType = randint(0, 1)
            if simpleWeaponType == 0:
                equiptment.append(simpleMeleeWeapons[randint(0, len(simpleMeleeWeapons) - 1)])
            else:
                equiptment.append(simpleRangedWeapons[randint(0, len(simpleRangedWeapons) - 1)])
        equiptment.append("Explorers Pack")
        equiptment.append("4 Javelins")

        self.equiptment = equiptment

    def getBarbarianSubclass(self):
        return random.choice(list(BarbarianSubclasses))
