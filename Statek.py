class Statek:
    def __init__(self, wielokat, pozycja_pocz, predkosc):
        self.wielokat = wielokat
        self.pozycja_poczatkowa = pozycja_pocz
        self.predkosc = predkosc

    def zaktualizuj_pozycje(self, punkt_odniesienia):
        for i in self.wielokat.punkty:
            i.x = i.x + self.predkosc.x
            i.y = i.y + self.predkosc.y

        punkt_odniesienia.x += self.predkosc.x
        punkt_odniesienia.y += self.predkosc.y