import math
from math import sin, cos

import Wyniki
import Calkowanie


def wybor_fun():
    wybrana = 0
    print("Wybierz rodzaj funkcji: \n"
          "1. funkcja trygometryczna\n"
          "2. fukcja wielomianowa\n"
          "3. funkcja zewneczna z  wartoscia bezwzgledna\n"
          "4. funkcja z wartoscia bezwzgledna |x| \n"
          "5. funkcja zlozona\n")
    choice = input("Twój wybór: ")

    if choice == "1":
        print("Wybór f. trygometrycznych:\n"
              "1. sin(x)\n"
              "2. cos(x)\n"
              "3. sin(2x)\n"
              "4. cos(2x)")
        choice2 = input("Twój wybór: ")
        if choice2 == "1":
            wybrana = sin
        elif choice2 == "2":
            wybrana = cos
        elif choice2 == "3":
            wybrana = Wyniki.oblicz_sin_2x
        elif choice2 == "5":
            wybrana = Wyniki.oblicz_cos_2x

    elif choice == "2":
        Wyniki.stopien = input("Podaj stopień wielomianu: ")
        Wyniki.wspolczynniki = [0 for _ in range(int(Wyniki.stopien) + 1)]
        for i in range(0, int(Wyniki.stopien) + 1):
            Wyniki.wspolczynniki[i] = int(
                input("Podaj wspołczynnik przy argumencie o potędze " + str(int(Wyniki.stopien) - i) + ": "))
        wybrana = Wyniki.horner

    elif choice == "3":
        print("Wybór funkcji w srodku modulu:\n"
              "1. wielomian \n"
              "2. trygonometryczna")
        choice_srodek = input("wybierz numer funkcji w srodku modulu")
        if choice_srodek == "1":
            Wyniki.stopien = input("Podaj stopień wielomianu: ")
            Wyniki.wspolczynniki = [0 for _ in range(int(Wyniki.stopien) + 1)]
            for i in range(0, int(Wyniki.stopien) + 1):
                Wyniki.wspolczynniki[i] = int(
                    input("Podaj wspołczynnik przy argumencie o potędze " + str(int(Wyniki.stopien) - i) + ": "))
            wybrana = Wyniki.bezwzgledna_wielomian
        elif choice_srodek == "2":
            print("Wybór f. trygometrycznych:\n"
                  "1. |sin(x)|\n"
                  "2. |cos(x)|\n"
                  "3. |sin(2x)|\n"
                  "4. |cos(2x)|")
            choice_trygonometryczna = input("Twój wybór: ")
            Wyniki.wolny =  float (input("Podaj wyraz wolny "))
            if choice_trygonometryczna == "1":
                print(" 1.Wyraz wolny w module ")
                print(" 2.Wyraz wolny poza modulem ")
                wybor = input("wolny w module czy poza?")
                if wybor == "1":
                    wybrana = Wyniki.abs_sin
                elif wybor == "2":
                    wybrana = Wyniki.abs_sin_wolnypoza
            elif choice_trygonometryczna == "2":
                print(" 1.Wyraz wolny w module ")
                print(" 2.Wyraz wolny poza modulem ")
                wybor = input("Wybor")
                if wybor == "1":
                    wybrana = Wyniki.abs_cos
                elif wybor == "2":
                    wybrana = Wyniki.abs_cos_wolnypoza
            elif choice_trygonometryczna == "3":
                print(" 1.Wyraz wolny w module ")
                print(" 2.Wyraz wolny poza modulem ")
                wybor = input("Wybor")
                if wybor == "1":
                    wybrana = Wyniki.oblicz_sin_2x_abs
                elif wybor == "2":
                    wybrana = Wyniki.abs_2sin_wolnypoza
            elif choice_trygonometryczna == "4":
                print(" 1.Wyraz wolny w module ")
                print(" 2.Wyraz wolny w module ")
                wybor =  (input("Wybor"))
                if wybor == "1":
                    wybrana = Wyniki.oblicz_cos_2x_abs
                elif wybor == "2":
                    wybrana = Wyniki.abs_2cos_wolnypoza


    elif choice == "4":
            print("Wybór f. trygometrycznych:\n"
                  "1. sin|x|\n"
                  "2. cos|x|\n"
                  "3. sin|2x|\n"
                  "4. cos|2x|")
            choice_trygonometryczna = input("Twój wybór: ")
            Wyniki.wolny = float (input("Podaj wyraz wolny "))
            if choice_trygonometryczna == "1":
                wybrana = Wyniki.sin_modul_x
            elif choice_trygonometryczna == "2":
                wybrana = Wyniki.cos_modul_x
            elif choice_trygonometryczna == "3":
                wybrana = Wyniki.sin_2x_modul_x
            elif choice_trygonometryczna == "4":
                wybrana = Wyniki.cos_2x_modul_x

    elif choice == "5":
        print("Wybierz funkcje zewneczna\n"
              "1. sin(x)\n"
              "2. cos(x)\n"
              "3. sin(2x)\n"
              "4. cos(2x)\n"
              "5. |sin(x)|\n"
              "6. |cos(x)|\n"
              "7. |sin(2x)|\n"
              "8. |cos(2x)|"
              )
        zewneczna = input("Podaj wybor: ")
        Wyniki.stopien = input("Wpisz stopien wielomianowej funkcje wewneczna: ")
        Wyniki.wspolczynniki = [0 for _ in range(int(Wyniki.stopien) + 1)]
        for i in range(0, int(Wyniki.stopien) + 1):
            Wyniki.wspolczynniki[i] = int(
                input("Podaj wspołczynnik przy argumencie o potędze " + str(int(Wyniki.stopien) - i) + ": "))
        if zewneczna == "1":
            wybrana = Wyniki.zlozenie_sin
        elif zewneczna == "2":
            wybrana = Wyniki.zlozenie_cos
        elif zewneczna == "3":
            wybrana = Wyniki.zlozenie_sin_2x
        elif zewneczna == "4":
            wybrana = Wyniki.zlozenie_cos_2x
        elif zewneczna == "5":
                wybrana = Wyniki.abs_zlozenie_sin
        elif zewneczna == "6":
                wybrana = Wyniki.abs_zlozenie_cos
        elif zewneczna == "7":
                wybrana = Wyniki.abs_zlozenie_sin_2x
        elif zewneczna == "8":
                wybrana = Wyniki.abs_zlozenie_cos_2x

    else:
        print("Zły wybór!!!")
    return wybrana

#wybor_fun()
print("Gaus czy Simpson? \n 1.Simpson\n 2.Gaus")
wybor = input("Twoj wybor ")
eps = float(input("Podaj dokladnosc calkowania "))
if wybor == "1":
    przedzial = input("1.Przedzial skonczony.\n2.Przedzual 0:inf ")
    if przedzial == "1":
        mini = float(input("Podaj poczatek calkowania "))
        maks = float(input("Podaj koniec calkowania "))
        print(Calkowanie.zlozona_metoda_simpsona(mini, maks, wybor_fun(), eps))
    elif przedzial == "2":
        print(Calkowanie.newton_cotes(wybor_fun(),eps))
elif wybor == "2":
    wezly = int(input("Podaj liczbe wezlow do metody Gausa"))
    print(Calkowanie.gauss(wybor_fun(),wezly))







