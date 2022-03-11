import random
from random import randint
from enum import Enum

class martialMeleeWeapons(str, Enum):
    BATTLEAXE   = "Battleaxe"
    FLAIL       = "Flail"
    GLAIVE      = "Glaive"
    GREATAXE    = "Greataxe"
    GREATSWORD  = "Greatsword"
    HALBERD     = "Halberd"
    LANCE       = "Lance"
    LONGSWORD   = "Longsword"
    MAUL        = "Maul"
    MORNINGSTAR = "Morningstar"
    PIKE        = "Pike"
    RAPIER      = "Rapier"
    SCIMITAR    = "Scimitar"
    SHORTSWORD  = "Shortsword"
    TRIDENT     = "Trident"
    WAR_PICK    = "War Pick"
    WARHAMMER   = "Warhammer"
    WHIP        = "Whip"

class martialRangedWeapons(str, Enum):
    BLOWGUN        = "Blowgun"
    CROSSBOW_HAND  = "Crossbow, Hand"
    CROSSBOW_HEAVY = "Crossbow, Heavy"
    LONGBOW        = "Longbow"
    NET            = "Net"

class simpleMeleeWeapons(str, Enum):
    CLUB         = "Club"
    DAGGER       = "Dagger"
    GREATCLUB    = "Greatclub"
    HANDAXE      = "Handaxe"
    JAVELIN      = "Javelin"
    LIGHT_HAMMER = "Light Hammer"
    MACE         = "Mace"
    QUARTERSTAFF = "Quarterstaff"
    SICKLE       = "Sickle"
    SPEAR        = "Spear"

class simpleRangedWeapons(str, Enum):
    LIGHT_CROSSBOW = "Light Crossbow"
    DART           = "Dart"
    SHORTBOW       = "Shortbow"
    SLING          = "Sling"

class musicalInstruments(str, Enum):
    BAGPIPES = "Bagpipes"
    DRUM = "Drum"
    DULCIMER = "Dulcimer"
    FLUTE = "Flute"
    LUTE = "Lute"
    LYRE = "Lyre"
    HORN = "Horn"
    PAN_FLUTE = "Pan flute"
    SHAWM = "Shawm"
    VIOL = "Viol"
    #TODO See musical instruments. Navigators tools?

class Weapons():

    def getMartialRangedWeapon(self):
        return random.choice(list(martialRangedWeapons))

    def getMartialMeleeWeapon(self):
        return random.choice(list(martialMeleeWeapons))

    def getMartialWeapon(self):
        if (randint(0, 1) == 0):
            return self.getMartialRangedWeapon()
        else:
            return self.getMartialMeleeWeapon()

    def getSimpleMeleeWeapon(self):
        return random.choice(list(simpleMeleeWeapons))

    def getSimpleRangedWeapon(self):
        return random.choice(list(simpleRangedWeapons))

    def getSimpleWeapon(self):
        if (randint(0, 1) == 0):
            return self.getSimpleMeleeWeapon()
        else:
            return self.getSimpleRangedWeapon()

    def getMusicalInstrument(self):
        return random.choice(list(musicalInstruments))
