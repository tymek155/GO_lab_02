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

    def otoczka(self, lista_punktow):
        punkt_min, punkt_max = self.max_min(lista_punktow)
        linia = Linia.Linia(punkt_min, punkt_max)
        prawa_cz, lewa_cz = self.podziel_punkty(lista_punktow, linia)
        prawa_cz.append(punkt_max)

        #tworzenie prawej strony
        punkt_poczatkowy = punkt_min
        lista_wynik = []
        lista_wynik.append(punkt_poczatkowy)
        wektor10 = Wektor.Wektor(1,0)
        start = prawa_cz[0]
        kat = wektor10.kat_miedzy_wektorami(Wektor.Wektor(start.x - punkt_min.x, start.y - punkt_max.y))

        iter = 0
        while(True):
            do_dodania = prawa_cz[0]
            kat = wektor10.kat_miedzy_wektorami(Wektor.Wektor(do_dodania.x - lista_wynik[0].x, do_dodania.y - lista_wynik[0].y))
            for i in range(1, len(prawa_cz)):
                spr_kat = wektor10.kat_miedzy_wektorami(Wektor.Wektor(prawa_cz[i].x - lista_wynik[iter].x, prawa_cz[i].y - lista_wynik[iter].y))
                if spr_kat < kat:
                    do_dodania = prawa_cz[i]
                    kat = spr_kat
            lista_wynik.append(do_dodania)
            prawa_cz.remove(do_dodania)
            if do_dodania == punkt_min:
                break




