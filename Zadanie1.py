import Read
import AlgorytmJarvisa
import AlgorytmGraham
import Wielokat
from Show import wyswietl_punkty, wyswietl_punkty_short, wyswietl_wielokat


class Zadanie1:
    def __init__(self):
        pass
    def pokaz_figury_1(self):
        r = Read.Read
        lista_punktow = []
        lista_punktow, ilosc = r.read_file("dane.txt")
        wyswietl_punkty(lista_punktow)

        jarvis = AlgorytmJarvisa.AlgorytmJarvisa()
        jlewa,jprawa = jarvis.otoczka(lista_punktow)
        wyswietl_punkty_short(jlewa)
        wyswietl_punkty(jprawa)

        lista_punktow, ilosc = r.read_file("dane.txt")

        graham = AlgorytmGraham.AlgorytmGraham()
        gOtoczka = graham.otoczka(lista_punktow, ilosc)
        wyswietl_punkty(gOtoczka)

    def pokaz_figury_2(self):
        r = Read.Read
        lista_punktow = []
        lista_punktow, ilosc = r.read_file("dane2.txt")
        wyswietl_punkty(lista_punktow)

        jarvis = AlgorytmJarvisa.AlgorytmJarvisa()
        jlewa, jprawa = jarvis.otoczka(lista_punktow)
        wyswietl_punkty_short(jlewa)
        wyswietl_punkty(jprawa)

        lista_punktow, ilosc = r.read_file("dane2.txt")

        graham = AlgorytmGraham.AlgorytmGraham()
        gOtoczka = graham.otoczka(lista_punktow, ilosc)
        wyswietl_punkty(gOtoczka)

    def figura_otoczka_1(self):
        r = Read.Read
        lista_punktow = []
        lista_punktow, ilosc = r.read_file("dane.txt")
        wyswietl_punkty_short(lista_punktow)

        jarvis = AlgorytmJarvisa.AlgorytmJarvisa()
        jlewa, jprawa = jarvis.otoczka(lista_punktow)
        jlewa.pop()
        jprawa.pop()
        jotoczka = jlewa + jprawa
        jwielokat = Wielokat.Wielokat(jotoczka)
        wyswietl_wielokat(jwielokat)

        lista_punktow, ilosc = r.read_file("dane.txt")
        wyswietl_punkty_short(lista_punktow)

        graham = AlgorytmGraham.AlgorytmGraham()
        gOtoczka = graham.otoczka(lista_punktow, ilosc)
        gwielokat = Wielokat.Wielokat(gOtoczka)
        wyswietl_wielokat(gwielokat)

    def figura_otoczka_2(self):
        r = Read.Read
        lista_punktow = []
        lista_punktow, ilosc = r.read_file("dane2.txt")
        wyswietl_punkty_short(lista_punktow)

        jarvis = AlgorytmJarvisa.AlgorytmJarvisa()
        jlewa, jprawa = jarvis.otoczka(lista_punktow)
        jlewa.pop()
        jprawa.pop()
        jotoczka = jlewa + jprawa
        jwielokat = Wielokat.Wielokat(jotoczka)
        wyswietl_wielokat(jwielokat)

        lista_punktow, ilosc = r.read_file("dane2.txt")
        wyswietl_punkty_short(lista_punktow)

        graham = AlgorytmGraham.AlgorytmGraham()
        gOtoczka = graham.otoczka(lista_punktow, ilosc)
        gwielokat = Wielokat.Wielokat(gOtoczka)
        wyswietl_wielokat(gwielokat)


