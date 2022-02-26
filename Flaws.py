from random import randint

class CharacterFlaws():
    flaws = ["Afraid of the dark",
             "Afraid of heights",
             "Has an unusually small bladder",
             "Tells really long stories with unnecessary details",
             "Has short term memory loss",
             "Color blind", #TODO: add types of color blindness subcatagory
             "Believes that every npc is out to get them",
             "Can't tell the difference between alive and undead",
             "Can't keep a secret",
             "Severe nut allergy",
             "Sleepwalks",
             "Doesn't like to sleep alone",
             "Really bad at remembering names"
             ]

    def getCharacterFlaws(self, dndclass):

        # Add any flaws specific to the class selected
        self.addClassFlaws(dndclass)

        # Array to hold character flaws
        characterFlaws = []

        # Character will have between 1 and 3 flaws
        numFlaws = randint(1, 3)

        for i in range(numFlaws):
            flawIndex = randint(0, len(self.flaws) - 1)
            characterFlaws.append(self.flaws[flawIndex])
            self.flaws.pop(flawIndex)

        return characterFlaws

    def addClassFlaws(self, dndclass):
        if dndclass == "Sorcerer":
            self.flaws.append("Phobia of casting spells with people watching")

        if dndclass == "Wizard":
            self.flaws.append("Phobia of casting spells with people watching")
