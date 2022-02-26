from random import randint
import random
from Subclasses import MonkSubclasses

class MonkDetails():

    def getMonkEquiptment(self, simpleMeleeWeapons, simpleRangedWeapons):
        equiptment = []
        num = randint(0, 1)
        if num == 0:
            equiptment.append("ShortSword")
        else:
             simpleWeaponType = randint(0, 1)
             if simpleWeaponType == 0:
                 equiptment.append(simpleMeleeWeapons[randint(0, len(simpleMeleeWeapons) - 1)])
             else:
                 equiptment.append(simpleRangedWeapons[randint(0, len(simpleRangedWeapons) - 1)])
        num = randint(0, 1)
        if num == 0:
            equiptment.append("Dungeoneer's pack")
        else:
            equiptment.append("Explorer's pack")
        equiptment.append("10 darts")
        return equiptment

    def getMonkSubclass(self):
        return random.choice(list(MonkSubclasses))
