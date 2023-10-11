def SET_BIT(x: int, p: int) -> int:
    return x | (1 << p)


def UNSET_BIT(x: int, p: int) -> int:
    return SET_BIT(x, p) ^ (1 << p)


def BIT_IS_SET(x: int, p: int) -> bool:
    return x & (1 << p) != 0


def BIT_AND(a: int, b: int) -> int:
    return a & b


def BIT_OR(a: int, b: int) -> int:
    return a | b


def BIT_XOR(a: int, b: int) -> int:
    return a ^ b


def BIT_NOT_8(x: int) -> int:
    return (~x) & 0xFF


def BIT_NOT_16(x: int) -> int:
    return (~x) & 0xFFFF


def BIT_NOT_32(x: int) -> int:
    return (~x) & 0xFFFFFFFF
