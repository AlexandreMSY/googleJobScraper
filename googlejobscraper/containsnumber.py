def containsNumber(string: str) -> bool:
    return any(chr.isdigit() for chr in string)
