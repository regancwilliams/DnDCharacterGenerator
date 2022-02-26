from Constants import Races, Genders
from random import randint
class Names():
    firstNames = []
    lastNames = []

    def getCharacterName(characterRace):

        # Add any names specific to the race selected
        self.addRaceNames(dndRace)

        return firstNames[randint(0, len(firstNames) - 1)]

    def addRaceNames(dndRace, gender):
        if dndRace == Races.DWARF:
            if gender == Genders.FEMALE:
                self.firstNames.append("Amber")
                self.firstNames.append("Artin")
                self.firstNames.append("Audhild")
                self.firstNames.append("Bardryn")
                self.firstNames.append("Dagnal")
                self.firstNames.append("Diesa")
                self.firstNames.append("Eldeth")
                self.firstNames.append("Falkrunn")
                self.firstNames.append("Finellen")
                self.firstNames.append("Gunnloda")
                self.firstNames.append("Gurdis")
                self.firstNames.append("Gurdis")
                self.firstNames.append("Helja")
                self.firstNames.append("Hlin")
                self.firstNames.append("Kathra")
                self.firstNames.append("Kristryd")
                self.firstNames.append("Ilde")
                self.firstNames.append("Liftrasa")
                self.firstNames.append("Mardred")
                self.firstNames.append("Riswynn")
                self.firstNames.append("Sannl")
                self.firstNames.append("Torbera")
                self.firstNames.append("Torgga")
                self.firstNames.append("Vistra")
            else if gender == Genders.MALE:
                self.firstNames.append("Adrik")
        else if dndRace == Races.DRAGONBORN:
            if gender == Genders.FEMALE:
                self.firstNames.append("Akra")
                self.firstNames.append("Biri")
                self.firstNames.append("Daar")
                self.firstNames.append("Farideh")
                self.firstNames.append("Harann")
                self.firstNames.append("Havilar")
                self.firstNames.append("Jheri")
                self.firstNames.append("Kava")
                self.firstNames.append("Korinn")
                self.firstNames.append("Mishann")
                self.firstNames.append ("Nala")
                self.firstNames.append("Perra")
                self.firstNames.append("Raiann")
                self.firstNames.append("Sora")
                self.firstNames.append("Surina")
                self.firstNames.append("Thava")
                self.firstNames.append("Uadjit")
            else if gender == Genders.MALE:
                self.firstNames.append("Arjhan")
        else if dndRace == Races.TIFLING:
            if gender == Genders.FEMALE:
                self.firstNames.append("Akta")
                self.firstNames.append("Anakis")
                self.firstNames.append("Bryseis")
                self.firstNames.append("Criella")
                self.firstNames.append("Damaia")
                self.firstNames.append("Ea")
                self.firstNames.append("Kallista")
                self.firstNames.append("Lerissa")
                self.firstNames.append("Makaria")
                self.firstNames.append("Nemeia")
                self.firstNames.append("Orianna")
                self.firstNames.append("Phelaia")
                self.firstNames.append("Rieta")
            else if gender == GENDERS.MALE:
                self.firstNames.append("Akmenos")
                self.firstNames.append("Amnon")
                self.firstNames.append("Barakas")
                self.firstNames.append("Damakos")
                self.firstNames.append("Ekemon")
                self.firstNames.append("Iados")
                self.firstNames.append("Kairon")
                self.firstNames.append("Leucis")
                self.firstNames.append("Melech")
                self.firstNames.append("Mordai")
                self.firstNames.append("Morthos")
                self.firstNames.append("Pelaios")
                self.firstNames.append("Skamos")
                self.firstNames.append("Therai")
