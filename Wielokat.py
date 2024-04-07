from Linia import Linia
from Punkt import Punkt

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
        roznica_x = punkt_odniesienia.x
        roznica_y = punkt_odniesienia.y

        for punkt in lista_punktow:
            punkt.x -= roznica_x
            punkt.y -= roznica_y