def SUBSTRING(string: str, start: int, end: int | None = None) -> str:
    return string[start:end] if end else string[start:]


def CHARACTER(string: str, index: int) -> str:
    return string[index]


def UPPERCASE(string: str) -> str:
    return string.upper()


def LOWERCASE(string: str) -> str:
    return string.lower()


def REPLACE(string: str, old, new) -> str:
    return string.replace(str(old), str(new))


def CONTAINS(string: str, substring: str) -> bool:
    return substring in string


def STRING_LENGTH(string: str) -> int:
    return len(string)


def REPEAT(string: str, n) -> str:
    return string * int(n)
