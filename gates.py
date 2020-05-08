# simulate AND, OR, NAND, XOR and NOT gates


def AND(a, b):
    return a & b


def OR(a, b):
    return a | b


def NAND(a, b):
    return 1 if not AND(a, b) else 0


def NOR(a, b):
    return 1 if not OR(a, b) else 0


def XOR(a, b):
    return 0 if a == b else 1


def NOT(a):
    return 1 if a == 0 else 0
