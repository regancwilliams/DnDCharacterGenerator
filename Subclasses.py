from enum import Enum

class BarbarianSubclasses(str, Enum):
    PATH_OF_THE_ANCESTRAL_GUARDIAN = "Path of the Ancestral Guardian"
    PATH_OF_THE_BATTLERANGER       = "Path of the Battleranger"
    PATH_OF_THE_BERSERKER          = "Path of the Berserker"
    PATH_OF_THE_STORM_HERALD       = "Path of the Storm Herald"
    PATH_OF_THE_TOTEM_WARRIOR      =  "Path of the Totem Warrior"
    PATH_OF_THE_ZEALOT             = "Path of the Zealot"

class BardSubclasses(str, Enum):
    COLLEGE_OF_CREATION  = "College of Creation"
    COLLEGE_OF_ELOQUENCE = "College of Eloquence"
    COLLEGE_OF_GLAMOUR   = "College of Glamour"
    COLLEGE_OF_LOVE      = "College of Lore"
    COLLGED_OF_SWORDS    = "College of Swords"
    COLLEGE_OF_VALOR     = "College of Valor"
    COLLEGE_OF_WHISPERS  = "College of Whispers"

class ClericSubclasses(str, Enum):
    ARCANA_DOMAIN   = "Arcana Domain"
    DEATH_DOMAIN    = "Death Domain"
    FORGE_DOMAIN    = "Forge Domain"
    GRAVE_DOMAIN    = "Grave Domain"
    KNOWLEGE_DOMAIN = "Knowledge Domain"
    LIFE_DOMAIN     = "Life Domain"
    LIGHT_DOMAIN    = "Light Domain"
    NATURE_DOMAIN   = "Nature Domain"
    ORDER_DOMAIN    = "Order Domain"
    PEACE_DOMAIN    = "Peace Domain"
    TEMPTEST_DOMAIN = "Temptest Domain"
    TRICKERY_DOMAIN = "Trickery Domain"
    TWILIGHT_DOMAIN = "Twilight Domain"
    WAR_DOMAIN      = "War Domain"

class DruidSubclasses(str, Enum):
    CIRCLE_OF_DREAMS       = "Circle of Dreams"
    CIRCLE_OF_STARS        = "Circle of Stars"
    CIRCLE_OF_WILDFIRE     = "Circle of Wildfire"
    CIRCLE_OF_LAND         = "Circle of the Land"
    CIRCLE_OF_THE_MOON     = "Circle of the Moon"
    CIRCLE_OF_THE_SHEPHERD = "Circle of the Shepherd"
    CIRCLE_OF_SPORES       = "Circle of Spores"

class FighterSubclasses(str, Enum):

    ARCANE_ARCHER        = "Arcane Archer"
    BATTLE_MASTER        = "Battle Master"
    CAVALIER             = "Cavalier"
    CHAMPION             = "Champion",
    ECHO_KNIGHT          = "Echo Knight"
    ELDRITCH_KNIGHT      = "Eldritch Knight"
    PSI_WARRIOR          = "Psi Warrior"
    PURPLE_DRAGON_KNIGHT = "Purple Dragon Knight"
    RUNE_KNIGHT          = "Rune Knight"
    SAMURAI              = "Samurai"

class MonkSubclasses(str, Enum):
    WAY_OF_THE_COBAALT_SOUL = "Way of the Cobalt Soul"
    WAY_OF_THE_OPEN_HAND    = "Way of the Open Hand"

class PaladinSubclasses(str, Enum):
    OATHBREAKER = "Oathbreaker" #TODO

class RangerSubclasses(str, Enum):
    RANGERSUBCLASS = "RangerSubclass here" #TODO

class RogueSubclasses(str, Enum):
    ARCANE_TRICKSTER = "Arcane Trickster"
    ASSASSIN         = "Assassin"
    INQUISITIVE      = "Inquisitive"
    MASTERMIND       = "Mastermind"
    SCOUT            = "Scout"
    SWASHBUCKLER     = "Swashbuckler"
    THIEF            = "Thief"

class SorcererSubclasses(str, Enum):
    SORCERERSUBCLASS = "SorcerSubclass here" #TODO
