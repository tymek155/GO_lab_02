from Linia import Linia
from Punkt import Punkt
import Wektor

class Wielokat:
    def __init__(self, wierzcholki):
        self.punkty = wierzcholki

    def sprawdz_przeciecia(self):
        opt, lista_linii = self.sprawdz_wielokat()
        if opt is False:
            return False
        else:
            for i in lista_linii:
                sum = 0
                for j in lista_linii:
                    if (i.przeciecie_linii(j) == True):
                        sum += 1
                if (sum > 2):
                    print("Nie można utworzyć wielokąta!")
                    return False
            print("Wielokat jest poprawny")
            return True

    def sprawdz_wielokat(self):
        lista_linii = []
        for i in range(0, len(self.punkty) - 1):
            lista_linii.append(Linia(self.punkty[i], self.punkty[i + 1]))
        lista_linii.append(Linia(self.punkty[-1], self.punkty[0]))

        for i in range(0, len(lista_linii)):
            if i == (len(lista_linii) - 1):
                punkt_przeciecia = lista_linii[i].przeciecie_prostych(lista_linii[0])
                if punkt_przeciecia is not None and punkt_przeciecia.__eq__n__(
                        lista_linii[i].pkt_2) and punkt_przeciecia.__eq__n__(lista_linii[0].pkt_1):
                    print("Utworzono wielokat!")
                    return True, lista_linii
                else:
                    print("Nie można utowrzyć wielokąta!")
                    return False
            punkt_przeciecia = lista_linii[i].przeciecie_prostych(lista_linii[i + 1])
            if punkt_przeciecia is None or (
                    punkt_przeciecia.__eq__n__(lista_linii[i].pkt_2) == 0 and punkt_przeciecia.__eq__n__(
                    lista_linii[i + 1].pkt_1) == 0):
                print("Nie można utowrzyć wielokąta!")
                return None

    def wyrownaj_punkty(self, lista_punktow, punkt_odniesienia):
        srednia_x = 0
        srednia_y = 0

        for i in lista_punktow:
            srednia_x += i.x
            srednia_y += i.y

        srednia_x = srednia_x/len(lista_punktow)
        srednia_y = srednia_y/len(lista_punktow)

        wektor_przesuniecia = Wektor.Wektor(punkt_odniesienia.x - srednia_x, punkt_odniesienia.y - srednia_y)

        #aktualizacja punktow
        for i in lista_punktow:
            i.x+=wektor_przesuniecia.x
            i.y+=wektor_przesuniecia.y

        return Punkt(srednia_x+ wektor_przesuniecia.x, srednia_y + wektor_przesuniecia.y)

    def sprawdz_przynaleznosc_punktu(self, punkt):
        lista_linii = []
        for i in range(0, len(self.punkty) - 1):
            lista_linii.append(Linia(self.punkty[i], self.punkty[i + 1]))
        lista_linii.append(Linia(self.punkty[-1], self.punkty[0]))

        y_pr = punkt.y
        x_min = self.punkty[0].x
        x_max = self.punkty[0].x
        for i in self.punkty:
            if i.x < x_min:
                x_min = i.x
            if i.x > x_max:
                x_max = i.x

        linia_przecinajaca = Linia(Punkt(x_min, y_pr), punkt)

        przeciecia = 0
        spr = 0
        for i in range(0, len(lista_linii)):
            opt, punkt_przeciecia = lista_linii[i].przeciecie_linii_ret_pkt(linia_przecinajaca)
            if opt == True:
                if (punkt_przeciecia.__eq__n__(lista_linii[i].pkt_1) == 0) and (
                        punkt_przeciecia.__eq__n__(lista_linii[i].pkt_2) == 0):
                    przeciecia += 1
                else:
                    if (i + 1) >= len(lista_linii):
                        if ((lista_linii[i].pkt_1.y < punkt_przeciecia.y) and (
                                lista_linii[0].pkt_2.y > punkt_przeciecia.y) or (
                                lista_linii[i].pkt_1.y > punkt_przeciecia.y) and (
                                lista_linii[0].pkt_2.y < punkt_przeciecia.y)):
                            przeciecia += 1
                            i = i + 1
                        else:
                            i = i + 1
                    else:
                        if ((lista_linii[i].pkt_1.y < punkt_przeciecia.y) and (
                                lista_linii[i + 1].pkt_2.y > punkt_przeciecia.y) or (
                                lista_linii[i].pkt_1.y > punkt_przeciecia.y) and (
                                lista_linii[i + 1].pkt_2.y < punkt_przeciecia.y)):
                            przeciecia += 1
                            i = i + 2
                        else:
                            i = i + 2

        if przeciecia != 0 and przeciecia % 2 != 0:
            return True
        else:
            return False