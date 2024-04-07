import Pocisk
import Punkt
import Read
import AlgorytmJarvisa
import Wektor
import Wielokat
import Statek
from Show import wyswietl_wielokat_short, wyswietl_punkt, zakoncz_rysowanie, komunikat_postrzal


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
        pozycja_poczatkowa, predkosc = read.wczytaj_dane_statek("space_craft3.txt")
        statek = Statek.Statek(wielokat_statek, pozycja_poczatkowa, predkosc)

        #Wczytaj dane o pociskach
        pociski = read.wczytaj_pociski("missles3.txt")


        #Wyrowanj statek
        punkt_odniesienia = statek.wielokat.wyrownaj_punkty(statek.wielokat.punkty, statek.pozycja_poczatkowa)

        #Wyswietl plansze
        iter_czas = 0
        aktywne_pociski = []
        while iter_czas <= 2.0:
            for i in aktywne_pociski:
                i.zaktualizuj_pozycje_pocisk()

            if iter_czas != 0:
                statek.zaktualizuj_pozycje(punkt_odniesienia)

            do_dodania = []
            for i in pociski:
                if i.czas_wykrycia <= iter_czas:
                    if i not in aktywne_pociski:
                        do_dodania.append(i)

            for i in do_dodania:
                i.zaktualizuj_pozycje_start()
            aktywne_pociski.extend(do_dodania)
            #aktywne_pociski.append(Pocisk.Pocisk(0.231, punkt_odniesienia, 0))

            for i in aktywne_pociski:
                if statek.wielokat.sprawdz_przynaleznosc_punktu(i.punkt) == True:
                    komunikat_postrzal(punkt_odniesienia)

            wyswietl_wielokat_short(statek.wielokat)
            for i in aktywne_pociski:
                wyswietl_punkt(i.punkt)
            zakoncz_rysowanie(punkt_odniesienia)

            iter_czas += 0.1






