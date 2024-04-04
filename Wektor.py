import math

class Wektor:
    def __init__(self, px , py):
        self.x = px
        self.y = py

    def dlg_wektora(self):
        return math.sqrt(self.x**2+self.y**2)

    def kat_miedzy_wektorami(self, wektor2):
        iloczyn_wek = self.x*wektor2.x + self.y*wektor2.y
        cos = iloczyn_wek / (self.dlg_wektora() * wektor2.dlg_wektora())
        kat_rad = math.acos(cos)
        kat_stopnie = math.degrees(kat_rad)
        return kat_stopnie
