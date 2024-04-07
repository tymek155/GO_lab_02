class Pocisk:
    def __init__(self, czas, wspolrzedne, predkosc):
        self.czas_wykrycia = czas
        self.punkt = wspolrzedne
        self.wektor = predkosc

    def zaktualizuj_pozycje_pocisk(self):
        self.punkt.x += self.wektor.x
        self.punkt.y += self.wektor.y