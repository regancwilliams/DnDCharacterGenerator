from random import randint
import random
from Subclasses import FighterSubclasses
class FighterDetails():

    def getFighterEquiptment(self, martialMeleeWeapons, martialRangedWeapons):

        # Array to hold fighter equiptment
        equiptment = []

        num = randint(0, 1)
        if num == 0:
            equiptment.append("Chain mail")
        elif num == 1:
            equiptment.append("Leather armor")
            equiptment.append("Longbow")
            equiptment.append("20 arrows")

        num = randint(0, 1)
        if num == 0:
            martialWeaponType = randint(0, 1)
            if martialWeaponType == 0:
                equiptment.append(martialMeleeWeapons[randint(0, len(martialMeleeWeapons) - 1)])
            else:
                equiptment.append(martialRangedWeapons[randint(0, len(martialRangedWeapons) - 1)])
            equiptment.append("Shield")
        else:
            martialWeaponType = randint(0, 1)
            if martialWeaponType == 0:
                equiptment.append(martialMeleeWeapons[randint(0, len(martialMeleeWeapons) - 1)])
            else:
                equiptment.append(martialRangedWeapons[randint(0, len(martialRangedWeapons) - 1)])
            martialWeaponType = randint(0, 1)
            if martialWeaponType == 0:
                equiptment.append(martialMeleeWeapons[randint(0, len(martialMeleeWeapons) - 1)])
            else:
                equiptment.append(martialRangedWeapons[randint(0, len(martialRangedWeapons) - 1)])

        num = randint(0,1)
        if num == 0:
            equiptment.append("A light crossbow")
            equiptment.append("20 bolts")
        else:
            equiptment.append("Two handaxes")

        num == randint(0, 1)
        if num == 0:
            equiptment.append("A dungeoneer's pack")
        else:
            equiptment.append("An explorer's pack")

        self.equiptment = equiptment

    def getFighterSubclass(self):
        return random.choice(list(FighterSubclasses))
