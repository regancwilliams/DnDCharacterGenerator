from random import randint
import random
import AbilityScores
from Classes import Barbarian, Bard, Cleric, Druid, Fighter, Monk, Paladin, Ranger, Rogue, Wizard
from Races import Dragonborn, Dwarf, Elf, Gnome, Tiefling
import Flaws
from Constants import *
from Character import Character

def main():

    names = ["ColdToes", "Karen", "Chad", "Namphootle", "Alarick", "Wrathion"]

    traits = ["Uses gender neutral pronouns"]

    simpleMeleeWeapons = ["Club", "Dagger", "Greatclub", "Handaxe", "Javelin", "Light Hammer", "Mace",
                          "Quarterstaff", "Sickle", "Spear"]

    simpleRangedWeapons = ["Crossbow light", "Dart", "Shortbow", "Sling"]

    martialMeleeWeapons = ["Battleaxe", "Flail", "Glaive", "Greataxe", "Greatsword", "Halberd", "Lance",
                           "Longsword", "Maul", "Morningstar", "Pike", "Rapier", "Scimitar", "Shortsword",
                           "Trident", "War Pick", "Warhammer", "Whip"]

    martialRangedWeapons = ["Blowgun", "Crossbow, hand", "Crossbow, heavy", "Longbow", "Net"]

    musicalInstruments = ["Bagpipes", "Drum", "Dulcimer", "Flute", "Lute", "Lyre", "Horn", "Pan Flute",
                          "Shawm", "Viol"] #TODO See musical instruments. Navigators tools?

    magicalItems = ["A sword that inflicts emotiional wounds", "A rope that is always slightly too short for what you want to use it for",
                    "Negative gold pieces", "Armour that becomes more effective the uglier the wearer"]

    randomCharacter = Character()

    equiptment = []

    subclass = "" #Can delete once all classes have getSubclass functions

    dndName = names[randint(0, len(names) - 1)]

    dndClass = random.choice(list(Classes))
    dndRace = random.choice(list(Races))
    dndAlignment = random.choice(list(Alignment))

    dndClass = "Cleric"
    dndRace = "Gnome"

    if dndClass == "Barbarian":
        randomCharacter = Barbarian.BarbarianDetails()
        equiptment = randomCharacter.getBarbarianEquiptment(simpleMeleeWeapons, simpleRangedWeapons, martialMeleeWeapons)
        subclass = randomCharacter.getBarbarianSubclass()

    elif dndClass == "Bard":
        randomCharacter = Bard.BardDetails()
        equiptment = randomCharacter.getBardEquiptment(simpleMeleeWeapons, simpleRangedWeapons, musicalInstruments)
        subclass = randomCharacter.getBardSubclass()

    elif dndClass == "Cleric":
        randomCharacter = Cleric.ClericDetails()
        equiptment = randomCharacter.getClericEquiptment(simpleMeleeWeapons, simpleRangedWeapons)
        subclass = randomCharacter.getClericSubclass()

    elif dndClass == "Druid":
        druid = Druid.DruidDetails()
        equiptment = druid.getDruidEquiptment(simpleMeleeWeapons, simpleRangedWeapons)
        subclass = druid.getDruidSubclass()

    elif dndClass == "Fighter":
        fighter = Fighter.FighterDetails()
        equiptment = fighter.getFighterEquiptment(martialMeleeWeapons, martialRangedWeapons)
        subclass = fighter.getFighterSubclass()

    elif dndClass == "Monk":
        monk = Monk.MonkDetails()
        equiptment = monk.getMonkEquiptment(simpleMeleeWeapons, simpleRangedWeapons)
        subclass = monk.getMonkSubclass()

    elif dndClass == "Paladin":
        paladin = Paladin.PaladinDetails()
        equiptment = paladin.getPaladinEquiptment()
        subclass = paladin.getPaladinSubclass()

    elif dndClass == "Ranger":
        randomCharacter = Ranger.RangerDetails()
        equiptment = randomCharacter.getRangerEquiptment()
        subclass = randomCharacter.getRangerSubclass()

    elif dndClass == "Rogue":
        rogue = Rogue.RogueDetails()
        equiptment = rogue.getRogueEquiptment()
        subclass = rogue.getRogueSubclass()

    elif dndClass == "Sorcerer":
        x = 4

    elif dndClass == "Warlock":
        x = 4

    elif dndClass == "Wizard":
            wizard = Wizard.WizardDetails()
            equiptment = wizard.getWizardEquiptment()
            subclass = wizard.getWizardSubclass()

    if dndRace == "Dragonborn":
        characterRace = Dragonborn.DragonbornDetails()
    elif dndRace == "Dwarf":
        characterRace = Dwarf.DwarfDetails()
    elif dndRace == "Elf":
        characterRace = Elf.ElfDetails()
    elif dndRace == "Gnome":
        characterRace = Gnome.GnomeDetails()
    elif dndRace == "Tifling":
        characterRace = Tiefling.TieflingDetails()

    abilityScore = AbilityScores.AbilityScores()

    randomCharacter.age = characterRace.getAge()
    randomCharacter.height = characterRace.getHeight()
    randomCharacter.weight = characterRace.getWeight()
    randomCharacter.speed = characterRace.getSpeed()

    # Generate Ability Scores
    #TODO: Optimize scores based on class
    randomCharacter.charisma = abilityScore.getRandomScore()
    randomCharacter.constitution = abilityScore.getRandomScore()
    randomCharacter.dexterity = abilityScore.getRandomScore()
    randomCharacter.intelligence = abilityScore.getRandomScore()
    randomCharacter.strength = abilityScore.getRandomScore()
    randomCharacter.wisdom = abilityScore.getRandomScore()

    # Get Ability Modifiers
    randomCharacter.charisma = abilityScore.getAbilityModifier(randomCharacter.charisma)
    randomCharacter.constitution = abilityScore.getAbilityModifier(randomCharacter.constitution)
    randomCharacter.dexterity = abilityScore.getAbilityModifier(randomCharacter.dexterity)
    randomCharacter.intelligence = abilityScore.getAbilityModifier(randomCharacter.intelligence)
    randomCharacter.strength = abilityScore.getAbilityModifier(randomCharacter.strength)
    randomCharacter.wisdom = abilityScore.getAbilityModifier(randomCharacter.wisdom)

    flaws = Flaws.CharacterFlaws()

    print "Class: " + dndClass + "      Subclass: " + subclass
    print "Name: " + dndName
    print "Race: " + dndRace
    print "Alignment: " + dndAlignment
    print "Flaws: " + str(flaws.getCharacterFlaws(dndClass))

    randomCharacter.printCharaterInfo()
if __name__ == '__main__':
    main()
