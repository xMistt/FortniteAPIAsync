from enum import Enum


class AccountType(Enum):
    EPIC = 'epic'
    PLAYSTATION = 'psn'
    XBOX = 'xbl'


class StatsTimeWindow(Enum):
    SEASON = 'season'
    LIFETIME = 'lifetime'


class StatsImage(Enum):
    ALL = 'all'
    KEYBOARD_AND_MOUSE = 'keyboardMouse'
    CONTROLLER = 'gamepad'
    TOUCH = 'touch'
