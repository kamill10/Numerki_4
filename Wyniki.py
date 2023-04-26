from math import sin, cos


wspolczynniki = []
stopien = 0
wolny = 0

def bezwzgledna_wielomian(x):
    return abs(horner(x))

def abs_sin(x):
    return abs(sin(x)+wolny)
def abs_cos(x):
    return abs(cos(x)+wolny)

def oblicz_sin_2x(x):
    return 2*sin(x)*cos(x)
def oblicz_cos_2x(x):
    return cos(x)**2-sin(x)**2

def oblicz_sin_2x_abs(x):
    return abs(2*sin(x)*cos(x)+wolny)
def oblicz_cos_2x_abs(x):
    return abs(cos(x)**2-sin(x)**2+wolny)
def horner(x):
    result = 0
    for i in range(len(wspolczynniki)):
        result = x*result + wspolczynniki[i]
    return result

def zlozenie_sin(x):
    return sin(horner(x))

def zlozenie_cos(x):
    return cos(horner(x))

def zlozenie_sin_2x(x):
    return oblicz_sin_2x(horner(x))

def zlozenie_cos_2x(x):
    return oblicz_cos_2x(horner(x))
def abs_zlozenie_sin(x):
    return abs(sin(horner(x)))

def abs_zlozenie_cos(x):
    return abs(cos(horner(x)))

def abs_zlozenie_sin_2x(x):
    return abs(oblicz_sin_2x(horner(x)))

def abs_zlozenie_cos_2x(x):
    return abs(oblicz_cos_2x(horner(x)))

def sin_modul_x(x):
    return sin(abs(x))+wolny


def cos_modul_x(x):
    return cos(abs(x))+wolny


def sin_2x_modul_x(x):
    return oblicz_sin_2x(abs(x))+wolny


def cos_2x_modul_x(x):
    return oblicz_cos_2x(abs(x))+wolny


def abs_sin_wolnypoza(x):
    return abs(sin(x))+wolny


def abs_cos_wolnypoza(x):
    return abs(cos(x)) + wolny


def abs_2sin_wolnypoza(x):
    return abs(oblicz_sin_2x(x))+wolny


def abs_2cos_wolnypoza(x):
    return abs(oblicz_cos_2x(x))+wolny