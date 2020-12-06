from random import randint

class ClericDetails():

    def getClericEquiptment(self, simpleMeleeWeapons, simpleRangedWeapons):
        equiptment = []
        num = randint(0, 1)
        if num == 0:
            equiptment.append("Mace")
        else:
            equiptment.append("Warhammer") #TODO if proficient?
        num = randint(0, 2)
        if num == 0:
            equiptment.append("Scale Mail")
        elif num == 1:
            equiptment.append("Leather armor")
        else:
            equiptment.append("Chain mail") #TODO if proficient?
        num = randint(0, 1)
        if num == 0:
            equiptment.append("Light crossbow & 20 bolts")
        else:
            simpleWeaponType = randint(0, 1)
            if simpleWeaponType == 0:
                equiptment.append(simpleMeleeWeapons[randint(0, len(simpleMeleeWeapons) - 1)])
            else:
                equiptment.append(simpleRangedWeapons[randint(0, len(simpleRangedWeapons) - 1)])
        num = randint(0, 1)
        if num == 0:
            equiptment.append("Priest's pack")
        else:
            equiptment.append("Explorer's pack")
        equiptment.append("Shield")
        equiptment.append("Holy symbol")
        return equiptment

    def getClericSubclass(self):
        subclasses = ["Arcana Domain",   "Death Domain",     "Forge Domain",
                      "Grave Domain",    "Knowledge Domain", "Life Domain",
                      "Light Domain",    "Nature Domain",    "Order Domain",
                      "Peace Domain",    "Temptest Domain",  "Trickery Domain",
                      "Twilight Domain", "War Domain"]

        subclass = subclasses[randint(0, len(subclasses) - 1)]

        return subclass
