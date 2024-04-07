import Punkt
from Punkt import Punkt

class Linia:
    def __init__(self, a: type[Punkt], b: type[Punkt]):
        self.pkt_1 = a
        self.pkt_2 = b

    def rownanie_prostej(self):
        if self.pkt_1.x == self.pkt_2.x:
            return 0, 0
        wspolczynnik_a = (self.pkt_1.y - self.pkt_2.y) / (self.pkt_1.x - self.pkt_2.x)
        wspolczynnik_b = (self.pkt_1.y * self.pkt_2.x - self.pkt_2.y * self.pkt_1.x) / (self.pkt_2.x - self.pkt_1.x)
        return wspolczynnik_a, wspolczynnik_b

    def rownanie_ogolne(self):
        if self.pkt_1.x == self.pkt_2.x:
            return 1, 0, (-self.pkt_1.x)
        else:
            A, C = self.rownanie_prostej()
            B = -1
            return A, B, C

    def polozenie_pkt_prosta(self, spr: type[Punkt]):
        A, B, C = self.rownanie_ogolne()
        if B == 0:
            if self.pkt_1.x == spr.x:
                print("Punkt leży na prostej.")
                return 2
            elif self.pkt_1.x > spr.x:
                print("Punkt leży po lewej stronie.")
                return 1
            else:
                print("Punkt leży po prawej stronie.")
                return 3

        wynik = A * spr.x + B * spr.y + C
        if wynik == 0:
            print("Punkt leży na prostej.")
            return 2
        elif wynik > 0:
            print("Punkt leży po lewej stronie.")
            return 3
        else:
            print("Punkt leży po prawej stronie.")
            return 1

    def przeciecie_prostych(self, prosta2):
        A1, B1, C1 = self.rownanie_ogolne()
        A2, B2, C2 = prosta2.rownanie_ogolne()
        if (A1 * B2 - A2 * B1) == 0:
            print("Proste rownolegle!")
            return None
        else:
            px = ((C2 * B1 - C1 * B2) / (A1 * B2 - A2 * B1))
            py = ((A2 * C1 - A1 * C2) / (A1 * B2 - A2 * B1))
            punkt_przec = Punkt(px, py)
            return punkt_przec

    def przeciecie_linii_ret_pkt(self, linia2):
        punkt = self.przeciecie_prostych(linia2)
        psx1 = min(self.pkt_1.x, self.pkt_2.x)
        psx2 = max(self.pkt_1.x, self.pkt_2.x)

        psy1 = min(self.pkt_1.y, self.pkt_2.y)
        psy2 = max(self.pkt_1.y, self.pkt_2.y)
        if (punkt != None):
            if punkt.x >= psx1 and punkt.x <= psx2 and punkt.y >= psy1 and punkt.y <= psy2:
                plx1 = min(linia2.pkt_1.x, linia2.pkt_2.x)
                plx2 = max(linia2.pkt_1.x, linia2.pkt_2.x)

                ply1 = min(linia2.pkt_1.y, linia2.pkt_2.y)
                ply2 = max(linia2.pkt_1.y, linia2.pkt_2.y)

                if punkt.x >= plx1 and punkt.x <= plx2 and punkt.y >= ply1 and punkt.y <= ply2:
                    print("Punkt lezy na przecieciu linii!")
                    return True, punkt
        return False, None