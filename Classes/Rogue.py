from Character import Character
from random import randint
import random
from Subclasses import RogueSubclasses

class RogueDetails(Character):

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

        self.equiptment = equiptment

    def getRogueSubclass(self):
        return random.choice(list(RogueSubclasses))
