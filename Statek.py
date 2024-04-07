class Statek:
    def __init__(self, wielokat, pozycja_pocz, predkosc):
        self.wielokat = wielokat
        self.pozycja_poczatkowa = pozycja_pocz
        self.predkosc = predkosc

    def zaktualizuj_pozycje(self):
        for i in self.wielokat:
            i.x = i.x + self.predkosc.x
            i.y = i.y + self.predkosc.y