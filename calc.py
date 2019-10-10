import math


def addition(x, y):
    return x + y


def subtraktion(x, y):
    return x - y


def multiplikation(x, y):
    return x * y


def division(x, y):
    return x / y


def quadrat(x):
    return x * x


def logarithmus(x):
    return math.log(x)


def wurzel(x):
    return math.sqrt(x)


def writefile(erg):
    f = open("ergebnis.txt", "a")
    f.write("\n" + erg)
    f.close()