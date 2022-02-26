from enum import Enum

class Alignment(str, Enum):
    LAWFUL_GOOD     = "Lawful Good"
    NEUTRAL_GOOD    = "Neutral Good"
    CHAOTIC_GOOD    = "Chaotic Good"
    LAWFUL_NEUTRAL  = "Lawful Neutral"
    TRUE_NEUTRAL    = "True Neutral"
    CHAOTIC_NEUTRAL = "Chaotic Neutral"
    LWAFUL_EVIL     = "Lawful Evil"
    NEUTRAL_EVIL    = "Neutral Evil"
    CHAOTIC_EVIL    = "Chaotic Evil"

class Classes(str, Enum):
    BARBARIAN = "Barbarian"
    BARD      = "Bard"
    CLERIC    = "Cleric"
    DRUID     = "Druid"
    FIGHTER   = "Fighter"
    MONK      = "Monk"
    PALADIN   = "Paladin"
    RANGER    = "Ranger"
    ROGUE     = "Rogue"
    SORCERER  = "Sorcerer"
    WARLOCK   = "Warlock"
    WIZARD    = "Wizard"

class Skills(Enum):
    ACROBATICS      = "Acrobatics"
    ANIMAL_HANDLING = "Animal Handling"
    ARCANA          = "Arcana"
    ATHLETICS       = "Athletics"
    DECEPTION       = "Deception"
    HISTORY         = "Hitory"
    INSIGHT         = "Insight"
    INTIMIDATION    = "Intimidation"
    INVESTIGATION   = "Investigation"
    MEDICINE        = "Medicine"
    NATURE          = "Nature"
    PERCEPTION      = "Perception"
    PERFORMANCE     = "Performance"
    PERSUASION      = "Persuasion"
    RELIGION        = "Religion"
    SLIGHT_OF_HAND  = "Slight of Hand"
    STEALTH         = "Stealth"
    SURVIVAL        = "Survival"

class Races(str, Enum):
    ELF        = "Elf"
    DRAGONBORN = "Dragonborn"
    DWARF      = "Dwarf"
    GNOME      = "Gnome"
    HALF_ELF   = "Half-Elf"
    HALFLING   = "Halfling"
    HALF_ORC   = "Half-Orc"
    TIFLING    = "Tifling"
    HUMAN      = "Human"

class Genders(Enum):
    FEMALE = "Female"
    MALE   = "Male"

class EquiptmentPacks(str, Enum):
    DUNGEONEERS_PACK = "Dungeoneer's Pack"
    EXPLORERS_PACK   = "Explorer's Pack"

class Languages(str, Enum):
    COMMON   = "Common"
    DWARVISH = "Dwarvish"
    ELVISH   = "Elvish"
    GNOMISH  = "Gnomish"
    INFERNAL = "Infernal"

class size(str, Enum):
    SMALL = "Small"
    MEDIUM = "Medium"
