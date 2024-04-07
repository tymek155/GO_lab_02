import Punkt
import Pocisk

class Read:
    def __init__(self):
        pass

    @staticmethod
    def read_file(filename):
        with open(filename, 'r') as plik:
            rozmiar = int(plik.readline())

            punkty = []

            for _ in range(rozmiar):
                linia = plik.readline().strip().split()
                x, y = map(int, linia)
                punkty.append(Punkt.Punkt(x, y))

        return punkty, rozmiar

    def wczytaj_dane_statek(self, filename):
        with open(filename, "r") as plik:
            linia1 = plik.readline().strip()
            x1, y1 = map(float, linia1.split())

            linia2 = plik.readline().strip()
            x2, y2 = map(float, linia2.split())

        return Punkt.Punkt(x1, y1), Punkt.Punkt(x2, y2)

    def wczytaj_pociski(self, filename):
        pociski = []
        with open(filename, "r") as plik:
            for linia in plik:
                dane = linia.strip().split()
                czas = float(dane[0])
                x1, y1, x2, y2 = map(float, dane[1:])
                pociski.append(Pocisk.Pocisk(czas, Punkt.Punkt(x1, y1), Punkt.Punkt(x2, y2)))
        return pociski