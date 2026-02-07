from enum import Enum, IntFlag


class AccountType(Enum):
    EPIC        = 'epic'
    PLAYSTATION = 'psn'
    XBOX        = 'xbl'


class StatsTimeWindow(Enum):
    SEASON   = 'season'
    LIFETIME = 'lifetime'


class StatsImage(Enum):
    ALL                = 'all'
    KEYBOARD_AND_MOUSE = 'keyboardMouse'
    CONTROLLER         = 'gamepad'
    TOUCH              = 'touch'
    NONE               = 'none'


class AESKeyFormat(Enum):
    HEX    = 'hex'
    BASE64 = 'base64'


class ResponseFlags(IntFlag):
    NONE                    = 0
    INCLUDE_PATHS           = 1 << 0
    INCLUDE_GAMEPLAY_TAGS   = 1 << 1
    INCLUDE_SHOP_HISTORY    = 1 << 2
