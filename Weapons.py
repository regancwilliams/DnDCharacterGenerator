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
