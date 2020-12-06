from random import randint

class BarbarianDetails():

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

        return equiptment

    def getBarbarianSubclass(self):
        subclasses = ["Path of the Berserker",    "Path of the Zealot",              "Path of the Battleranger",
                      "Path of the Storm Herald", "Path of the Ancestral Guardian",  "Path of the Totem Warrior"]
        subclass = subclasses[randint(0, len(subclasses) - 1)]

        return subclass
