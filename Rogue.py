from random import randint

class RogueDetails():

    def getRogueEquiptment(self):

        # Array to hold all rogue equiptment
        equiptment = []

        num = randint(0, 1)
        if num == 0:
            equiptment.append("Rapier")
        else:
            equiptment.append("Shortsword")

        if "Shortsword" in equiptment:
            equiptment.append("A shortbow and quiver of 20 arrows")
        else:
            num = randint(0,1)
            if num == 0:
                equiptment.append("A shortbow and quiver of 20 arrows")
            else:
                equiptment.append("Shortsword")

        num = randint(0, 2)
        if num == 0:
            equiptment.append("A burglar's pack")
        elif num == 1:
            equiptment.append("A dungeoneer's pack")
        else:
            equiptment.append("An explorer's pack")

        equiptment.append("Leather armor")
        equiptment.append("Two daggers")
        equiptment.append("Thieves' tools")

        return equiptment

        def getRogueSubclass(self):
            subClasses = ["Arcane Trickster", "Assassin", "Inquisitive",
                          "Mastermind",       "Scout",    "Swashbuckler",
                          "Thief"]

            subclass = subclasses[randint(0, len(subclasses) - 1)]

            return subclass
