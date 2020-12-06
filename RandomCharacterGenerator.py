from random import randint
import Barbarian, Bard, Cleric, Druid, Fighter, Rogue, Wizard
import Flaws

def main():
    classes = ["Barbarian", "Bard", "Cleric", "Druid", "Fighter", "Monk", "Paladin", "Ranger",
                "Rogue", "Sorcerer", "Warlock", "Wizard"]

    races = ["Dragonborn", "Dwarf", "Elf", "Gnome", "Half-Elf", "Halfling", "Half-Orc", "Tifling",
            "Human"]

    alignments = ["Lawful Good", "Neutral Good", "Chaotic Good", "Lawful Neutral", "True Neutral",
                "Chaotic Neutral", "Lawful Evil", "Neutral Evil", "Chaotic Evil"]

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

    equiptment = []

    subclass = "" #Can delete once all classes have getSubclass functions

    dndName = names[randint(0, len(names) - 1)]
    dndClass = classes[randint(0, len(classes) - 1)]
    dndRace = races[randint(0, len(races) - 1)]
    dndAlignment = alignments[randint(0, len(alignments) - 1)]

    if dndClass == "Barbarian":
        barbarian = Barbarian.BarbarianDetails()
        equiptment = barbarian.getBarbarianEquiptment(simpleMeleeWeapons, simpleRangedWeapons, martialMeleeWeapons)
        subclass = barbarian.getBarbarianSubclass()

    elif dndClass == "Bard":
        bard = Bard.BardDetails()
        equiptment = bard.getBardEquiptment(simpleMeleeWeapons, simpleRangedWeapons, musicalInstruments)
        subclass = bard.getBardSubclass()

    elif dndClass == "Cleric":
        cleric = Cleric.ClericDetails()
        equiptment = cleric.getClericEquiptment(simpleMeleeWeapons, simpleRangedWeapons)
        subclass = cleric.getClericSubclass()

    elif dndClass == "Druid":
        druid = Druid.DruidDetails()
        equiptment = druid.getDruidEquiptment(simpleMeleeWeapons, simpleRangedWeapons)
        subclass = druid.getDruidSubclass()

    elif dndClass == "Fighter":
        fighter = Fighter.FighterDetails()
        equiptment = fighter.getFighterEquiptment(martialMeleeWeapons, martialRangedWeapons)
        subclass = fighter.getFighterSubclass()

    elif dndClass == "Monk":
        x = 4

    elif dndClass == "Paladin":
        x = 4

    elif dndClass == "Ranger":
        x = 4

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

    flaws = Flaws.CharacterFlaws()

    print "Class: " + dndClass + "      Subclass: " + subclass
    print "Name: " + dndName
    print "Race: " + dndRace
    print "Alignment: " + dndAlignment
    print "Equiptment: " + str(equiptment)
    print "Flaws: " + str(flaws.getCharacterFlaws(dndClass))

if __name__ == '__main__':
    main()
