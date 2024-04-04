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
            return 1
        else:
            print("Punkt leży po prawej stronie.")
            return 3