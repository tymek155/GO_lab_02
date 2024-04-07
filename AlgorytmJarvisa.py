import Linia
import Wektor

class AlgorytmJarvisa:
    def __init__(self):
        pass

    def max_min(self, lista_punktow):
        # szukanie y min
        punkt_min = lista_punktow[0]
        count = 0
        for i in lista_punktow:
            if i.y < punkt_min.y:
                punkt_min = i
                count = count + 1

        if count > 1:
            for i in lista_punktow:
                if i.y == punkt_min.y and i.x < punkt_min.x:
                    punkt_min = i

        # szukanie y max
        punkt_max = lista_punktow[0]
        count = 0
        for i in lista_punktow:
            if i.y > punkt_max.y:
                punkt_max = i
                count = count + 1

        if count > 1:
            for i in lista_punktow:
                if i.y == punkt_min.y and i.x > punkt_min.x:
                    punkt_min = i

        return punkt_min, punkt_max

    def podziel_punkty(self, lista_punktow, linia):
        prawe = []
        lewe = []
        for i in lista_punktow:
            if linia.polozenie_pkt_prosta(i) == 1:
                prawe.append(i)
            elif linia.polozenie_pkt_prosta(i) == 3:
                lewe.append(i)
        return prawe, lewe

    def sprawdz_strone(self, czesc, wektor10, punkt_poczatkowy, punkt_kon):
        lista_wynik = []
        lista_wynik.append(punkt_poczatkowy)

        iter = 0
        while (True):
            do_dodania = czesc[0]
            if do_dodania.x - lista_wynik[iter].x == 0 and do_dodania.y - lista_wynik[iter].y == 0:
                continue
            kat = wektor10.kat_miedzy_wektorami(Wektor.Wektor(do_dodania.x - lista_wynik[iter].x, do_dodania.y - lista_wynik[iter].y))
            for i in range(1, len(czesc)):
                if czesc[i].x - lista_wynik[iter].x == 0 and czesc[i].y - lista_wynik[iter].y == 0:
                    continue
                spr_kat = wektor10.kat_miedzy_wektorami(Wektor.Wektor(czesc[i].x - lista_wynik[iter].x, czesc[i].y - lista_wynik[iter].y))
                if spr_kat < kat:
                    do_dodania = czesc[i]
                    kat = spr_kat
            lista_wynik.append(do_dodania)
            czesc.remove(do_dodania)
            iter = iter + 1
            if do_dodania == punkt_kon:
                break
        return lista_wynik

    def otoczka(self, lista_punktow):
        punkt_min, punkt_max = self.max_min(lista_punktow)
        linia = Linia.Linia(punkt_min, punkt_max)
        prawa_cz, lewa_cz = self.podziel_punkty(lista_punktow, linia)
        prawa_cz.append(punkt_max)
        lewa_cz.append(punkt_min)

        #Tworzenie prawej i lewej storny
        wektor10 = Wektor.Wektor(1,0)
        wektor_10 = Wektor.Wektor(-1, 0)

        prawa_otoczka = self.sprawdz_strone(prawa_cz, wektor10, punkt_min, punkt_max)
        lewa_otoczka = self.sprawdz_strone(lewa_cz, wektor_10, punkt_max, punkt_min)
        return lewa_otoczka, prawa_otoczka




