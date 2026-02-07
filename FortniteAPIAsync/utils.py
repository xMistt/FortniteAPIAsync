from .enums import ResponseFlags

def combine_flags(flags: list[ResponseFlags]) -> int:
    return sum(flags, ResponseFlags.NONE)
