import Punkt

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

