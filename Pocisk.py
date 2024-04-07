class Pocisk:
    def __init__(self, czas, wspolrzedne, predkosc):
        self.czas_wykrycia = czas
        self.punkt = wspolrzedne
        self.wektor = predkosc

    def zaktualizuj_pozycje_pocisk(self):
        self.punkt.x += self.wektor.x
        self.punkt.y += self.wektor.y

    def zaktualizuj_pozycje_start(self):
        if abs(0.1 - self.czas_wykrycia) != 0:
            wspolczynik = (abs(0.1 - self.czas_wykrycia)) / 0.1
            self.punkt.x += self.wektor.x * wspolczynik
            self.punkt.y += self.wektor.y * wspolczynik
