from enum import Enum

class Speed(Enum):
    DRAGONBORN_SPEED = 30
    DWARF_SPEED      = 25
    ELF_SPEED        = 30
    GNOME_SPEED      = 25
    TIEFLING_SPEED   = 30

class Age(Enum):
    DRAGONBORN_MIN_AGE = 15
    DRAGONBORN_MAX_AGE = 85
    DWARF_MIN_AGE      = 25
    DWARF_MAX_AGE      = 375
    ELF_MIN_AGE        = 75
    ELF_MAX_AGE        = 750
    GNOME_MIN_AGE      = 20
    GNOME_MAX_AGE     = 500
    TIEFLING_MIN_AGE   = 12
    TIEFLING_MAX_AGE   = 100

# Weight in Pounds
class Weight(Enum):
    DRAGONBORN_MIN_WEIGHT = 200
    DRAGONBORN_MAX_WEIGHT = 300
    DWARF_MIN_WEIGHT      = 100
    DWARF_MAX_WEIGHT      = 200
    ELF_MIN_WEIGHT        = 100
    ELF_MAX_WEIGHT        = 175
    GNOME_MIN_WEIGHT      = 30
    GNOME_MAX_WEIGHT      = 50

# Height in Inches
class Height(Enum):
    DRAGONBORN_MIN_HEIGHT = 72
    DRAGONBORN_MAX_HEIGHT = 90
    DWARF_MIN_HEIGHT      = 48
    DWARF_MAX_HEIGHT      = 60
    ELF_MIN_HEIGHT        = 55
    ELF_MAX_HEIGHT        = 77
    GNOME_MIN_HEIGHT      = 36
    GNOME_MAX_HEIGHT      = 48
