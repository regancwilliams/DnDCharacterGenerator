from random import randint
import random
from Subclasses import DruidSubclasses
class DruidDetails():

    def getDruidEquiptment(self, simpleMeleeWeapons, simpleRangedWeapons):

        # Array to hold Druid equiptment
        equiptment = []

        num = randint(0, 1)
        if num == 0:
            equiptment.append("A wooden shield")
        elif num == 1:
             simpleWeaponType = randint(0, 1)
             if simpleWeaponType == 0:
                 equiptment.append(simpleMeleeWeapons[randint(0, len(simpleMeleeWeapons) - 1)])
             else:
                 equiptment.append(simpleRangedWeapons[randint(0, len(simpleRangedWeapons) - 1)])

        num = randint(0, 1)
        if num == 0:
            equiptment.append("A schimitar")
        else:
            equiptment.append(simpleMeleeWeapons[randint(0, len(simpleMeleeWeapons) - 1)])

        equiptment.append("Leather armor")
        equiptment.append("An explorer's pack")
        equiptment.append("Druidic focus")

        return equiptment

    def getDruidSubclass(self):
        return random.choice(list(DruidSubclasses))
