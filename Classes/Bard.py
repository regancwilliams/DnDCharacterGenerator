from random import randint
import random
from Subclasses import BardSubclasses
from Character import Character

class BardDetails(Character):

    def __init__(self):
        self.height = 1
        self.age = 1

    def getBardEquiptment(self, simpleMeleeWeapons, simpleRangedWeapons, musicalInstruments):
        equiptment = []
        num = randint(0, 2)
        if num == 0:
            equiptment.append("Rapier")
        elif num == 1:
            equiptment.append("Longsword")
        else:
             simpleWeaponType = randint(0, 1)
             if simpleWeaponType == 0:
                 equiptment.append(simpleMeleeWeapons[randint(0, len(simpleMeleeWeapons) - 1)])
             else:
                 equiptment.append(simpleRangedWeapons[randint(0, len(simpleRangedWeapons) - 1)])
        num = randint(0, 1)
        if num == 0:
            equiptment.append("Diplomat's pack")
        else:
            equiptment.append("Entertainer's pack")
        equiptment.append(musicalInstruments[randint(0, len(musicalInstruments) - 1)])
        equiptment.append("Leather armor")
        equiptment.append("1 dagger")
        
        self.equiptment = equiptment

    def getBardSubclass(self):
        return random.choice(list(BardSubclasses))
