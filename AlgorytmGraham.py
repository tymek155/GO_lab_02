import Wektor
import Linia

class AlgorytmGraham:
    def __init__(self):
        pass

    def min(self, lista_punktow):
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

        return punkt_min

    def ort(self, a, b, c):
        wart = ((b.y-a.y)*(c.x-b.x)-(b.x-a.x)*(c.y-b.y))
        if wart == 0:
            return 0
        elif wart > 0:
            return 1
        else:
            return 2

    def otoczka(self, punkty, ilosc):
        punkt_min = self.min(punkty)
        index_min = punkty.index(punkt_min)
        punkty[0], punkty[index_min] = punkty[index_min], punkty[0]
        wektor10 = Wektor.Wektor(1,0)

        #Sortowanie
        for i in range(1, ilosc):
            for j in range(1, ilosc-i):
                if wektor10.kat_miedzy_wektorami(Wektor.Wektor(punkty[j].x - punkty[0].x, punkty[j].y - punkty[0].y)) > wektor10.kat_miedzy_wektorami(Wektor.Wektor(punkty[j+1].x - punkty[0].x, punkty[j+1].y - punkty[0].y)):
                    punkty[j], punkty[j+1] = punkty[j+1], punkty[j]

        do_usuniecia = []
        tolerancja_katowa = 0.1

        for i in range(1, len(punkty)):
            for j in range(1, len(punkty)):
                if i == j:
                    continue
                kat_i = wektor10.kat_miedzy_wektorami(Wektor.Wektor(punkty[i].x - punkty[0].x, punkty[i].y - punkty[0].y))
                kat_j = wektor10.kat_miedzy_wektorami(Wektor.Wektor(punkty[j].x - punkty[0].x, punkty[j].y - punkty[0].y))
                # Sprawdzenie czy różnica między kątami jest mniejsza niż tolerancja_katowa
                if abs(kat_i - kat_j) < tolerancja_katowa:
                    if Wektor.Wektor(punkty[i].x - punkty[0].x,punkty[i].y - punkty[0].y).dlg_wektora() > Wektor.Wektor(punkty[j].x - punkty[0].x, punkty[j].y - punkty[0].y).dlg_wektora():
                        if punkty[j] not in do_usuniecia:
                            do_usuniecia.append(punkty[j])
                    else:
                        if punkty[i] not in do_usuniecia:
                            do_usuniecia.append(punkty[i])

        for i in do_usuniecia:
            punkty.remove(i)

        lista_otoczka = []
        lista_otoczka.append(punkty[0])
        lista_otoczka.append(punkty[1])
        lista_otoczka.append(punkty[2])

        for i in range(3, len(punkty)):
            while len(lista_otoczka) and self.ort(lista_otoczka[-2], lista_otoczka[-1], punkty[i]) != 2:
                lista_otoczka.pop()
            lista_otoczka.append(punkty[i])

        return lista_otoczka