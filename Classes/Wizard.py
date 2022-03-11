from Character import Character
from random import randint

class WizardDetails(Character):

    def getWizardEquiptment(self):
        equiptment = []
        num = randint(0, 1)
        if num == 0:
            equiptment.append("Quarterstaff")
        else:
            equiptment.append("Dagger")
        num = randint(0, 1)
        if num == 0:
            equiptment.append("Component Pouch")
        else:
            equiptment.append("Arcane Focus")
        num = randint(0, 1)
        if num == 0:
            equiptment.append("Scholars Pack")
        else:
            equiptment.append("Explorers Pack")
        equiptment.append("Spellbook")
        self.equiptment = equiptment

    def getWizardSubclass(self):
        subclasses = ["School of Transmutation", "School of Enchantment", "School of Abjuration",
                      "School of War Magic",     "School of Divination",  "School of Conjuration",
                      "School of Necromancy",    "School of Illusion",    "School of Bladesong",
                      "School of Evocation"]
        subclass = subclasses[randint(0, len(subclasses) - 1)]

        return subclass
