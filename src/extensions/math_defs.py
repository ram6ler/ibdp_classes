import math

type num = int | float

# Trigonometry.

PI = math.pi


def TO_DEGREES(x: num) -> float:
    return math.degrees(x)


def TO_RADIANS(x: num) -> float:
    return math.radians(x)


def SIN(x: num) -> float:
    return math.sin(x)


def COS(x: num) -> float:
    return math.cos(x)


def TAN(x: num) -> float:
    return math.tan(x)


def ARCSIN(x: num) -> float:
    return math.asin(x)


def ARCCOS(x: num) -> float:
    return math.acos(x)


def ARCTAN(x: num) -> float:
    return math.atan(x)


# Logarithms and exponentiation.

E = math.e


def LOG(x: num, b=10) -> float:
    return math.log(x, b)


def LN(x: num) -> float:
    return math.log(x)


def EXP(x: num) -> float:
    return math.exp(x)


def POWER(x: num, p: num) -> float:
    return math.pow(x, p)


def SQUARE(x: num) -> float:
    return x**2


def SQUARE_ROOT(x: num) -> float:
    return math.sqrt(x)
