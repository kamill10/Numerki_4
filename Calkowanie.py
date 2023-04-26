import math




def metoda_simpsona(a, b, f):
    h = (b - a) / 2
    calka = h*(f(a)*math.e**(-a) + 4*f((a+b)/2)*math.e**(-(a+b)/2) + f(b)*math.e**(-b))/3
    return calka


def zlozona_metoda_simpsona(poczatek_przedzialu, koniec_przedzialu, f, eps):
    calka = metoda_simpsona(poczatek_przedzialu, koniec_przedzialu, f)
    warunek = True
    n = 2
    while warunek:
        nowa_calka = 0
        h = (koniec_przedzialu - poczatek_przedzialu) / ( 2*n)       # n - liczba podprzedzialow
        a = poczatek_przedzialu
        b = a + 2 * h
        for i in range(n):
            i = metoda_simpsona(a, b, f)
            nowa_calka += i
            a = b
            b += 2 * h
        if abs(nowa_calka - calka) < eps:
            warunek = False
            calka = nowa_calka
        else:
            calka = nowa_calka
            n += 1
    return calka


def newton_cotes(f, eps):
    """
    :return: wartość kwadratury Newtona-Cotes'a na przedziale <0, infinity) (float)
    """
    a = 0
    delta = 1
    suma = 0
    jest = True
    while jest:
        calka = zlozona_metoda_simpsona(a, a + delta, f, eps)
        suma += calka
        a += delta
        if abs(calka) <= abs(eps):
            jest = False
    return suma


def wspolczynniki(liczba_wezlow, numer_wezla):
    dane = (
            ((0.585789, 0.853553), (3.414214, 0.146447)),
            ((0.415775, 0.711093), (2.294280, 0.278518), (6.289945, 0.010389)),
            ((0.322548, 0.603154), (1.745761, 0.357419), (4.536620, 0.038888), (2.395071, 0.000539)),
            ((0.263560, 0.521756), (1.413403, 0.398667), (3.596426, 0.075942), (7.085810, 0.003612), (12.640801, 0.000032))
            )
    return dane[liczba_wezlow - 2][numer_wezla]


def gauss(f, liczba_wezlow):
    """
    obliczanie wartości kwadratury Gaussa na podstawie tabeli
    :param wybor_funkcji: wybor funkcji z dostępnych(String)
    :param liczba_wezlow: liczba węzłów (int)
    :return: wartość kwadratyr Gaussa-Laugerre'a dla <0, inf)
    """
    calka = 0
    for i in range(liczba_wezlow):
        x = (wspolczynniki(liczba_wezlow, i)[0])
        w = (wspolczynniki(liczba_wezlow, i)[1])
        calka += w * f(x)
    return calka
