class Character:

    def __init__(self):
        self.age = 0
        self.height = 0
        self.weight = 0
        self.equiptment = []
        self.speed = 0

        # Ability Scores
        self.charisma = 0
        self.constitution = 0
        self.dexterity = 0
        self.intelligence = 0
        self.strength = 0
        self.wisdom = 0


    def printCharaterInfo(self):
        print "Height: "       + str(self.height)
        print "Age: "          + str(self.age)
        print "Weight: "       + str(self.weight)
        print "Speed: "        + str(self.speed)
        print "Equiptment: "   + str(self.equiptment)
        print "Charisma: "     + str(self.charisma)
        print "Constitution: " + str(self.constitution)
        print "Dexterity: "    + str(self.dexterity)
        print "Intelligence: " + str(self.intelligence)
        print "Strength: "     + str(self.strength)
        print "Wisdom: "       + str(self.wisdom)
