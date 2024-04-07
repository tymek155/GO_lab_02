import Read
import AlgorytmJarvisa
import Wektor
import Wielokat
import Statek
from Show import wyswietl_wielokat_short, wyswietl_punkty_short


class Zadanie2:
    def __init__(self):
        pass

    def plansza(self):
        read = Read.Read()
        lista_pkt_statek, ilosc = read.read_file("craft.txt")

        #Wczytaj statek
        algorytm_jarvisa = AlgorytmJarvisa.AlgorytmJarvisa()
        jlewa, jprawa = algorytm_jarvisa.otoczka(lista_pkt_statek)
        jlewa.pop()
        jprawa.pop()
        jotoczka = jlewa + jprawa
        wielokat_statek = Wielokat.Wielokat(jotoczka)

        #Wczytaj dane o statku
        pozycja_poczatkowa, predkosc = read.wczytaj_dane_statek("space_craft1.txt")
        statek = Statek.Statek(wielokat_statek, pozycja_poczatkowa, predkosc)

        #Wczytaj dane o pociskach
        pociski = read.wczytaj_pociski("missles2.txt")


        #Wyrowanj statek
        statek.wielokat.wyrownaj_punkty(statek.wielokat, statek.pozycja_poczatkowa)

        #Wyswietl plansze
        iter_czas = 0
        aktywne_pociski = []
        while iter_czas <= 2.0:
            for i in aktywne_pociski:
                i.zaktualizuj_pozycje_pocisk()

            if iter_czas != 0:
                statek.zaktualizuj_pozycje()

            for i in pociski:
                if i.czas_wykrycia <= iter_czas:
                    if i not in aktywne_pociski:
                        aktywne_pociski.append(i)

            wyswietl_wielokat_short(statek)
            for i in aktywne_pociski:
                wys


            iter_czas += 0.1






