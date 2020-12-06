from random import randint

class BardDetails():

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
        return equiptment

        def getBardSubclass(self):
            subclasses = ["College of Creation", "College of Eloquence", "College of Glamour",
                          "College of Lore",     "College of Swords",    "College of Valor",
                          "College of Whispers"]
            subclass = subclasses[randint(0, len(subclasses) - 1)]

            return subclass
