import matplotlib.pyplot as plt
from Linia import Linia

def wyswietl_linie_short(linia):
    plt.plot([linia.pkt_1.x, linia.pkt_2.x], [linia.pkt_1.y, linia.pkt_2.y], color="red")
    ax = plt.gca()
    ax.set_aspect('equal', adjustable='box')

def wyswietl_linie(linia):
    plt.plot([linia.pkt_1.x, linia.pkt_2.x], [linia.pkt_1.y, linia.pkt_2.y], color="red")
    plt.xlabel("OŚ X")
    plt.ylabel("OŚ Y")
    plt.title("Układ współrzędnych")
    plt.grid(True)
    ax = plt.gca()
    ax.set_aspect('equal', adjustable='box')
    plt.show()

def wyswietl_punkty(lista_pkt):
    for i in lista_pkt:
        plt.scatter(i.x, i.y, color="blue")
    plt.xlabel("OŚ X")
    plt.ylabel("OŚ Y")
    plt.title("Układ współrzędnych")
    plt.grid(True)
    ax = plt.gca()
    ax.set_aspect('equal', adjustable='box')
    plt.show()

def wyswietl_punkty_short(lista_pkt):
    for i in lista_pkt:
        plt.scatter(i.x, i.y, color="blue")
    plt.xlabel("OŚ X")
    plt.ylabel("OŚ Y")
    plt.title("Układ współrzędnych")
    plt.grid(True)
    ax = plt.gca()
    ax.set_aspect('equal', adjustable='box')

def wyswietl_punkt(punkt):
    plt.scatter(punkt.x, punkt.y, color="blue")

def wyswietl_wielokat(wielokat):
    #if wielokat.sprawdz_przeciecia() == False:
    #    return None
    for i in range(0, len(wielokat.punkty) -1):
        wyswietl_linie_short(Linia(wielokat.punkty[i], wielokat.punkty[i+1]))
    #plt.axis('square')
    wyswietl_linie(Linia(wielokat.punkty[0], wielokat.punkty[len(wielokat.punkty)-1]))

def wyswietl_wielokat_short(wielokat):
    #if wielokat.sprawdz_przeciecia() == False:
    #    return None
    for i in range(0, len(wielokat.punkty) -1):
        wyswietl_linie_short(Linia(wielokat.punkty[i], wielokat.punkty[i+1]))
    #plt.axis('square')
    wyswietl_linie_short(Linia(wielokat.punkty[0], wielokat.punkty[len(wielokat.punkty)-1]))

def zakoncz_rysowanie(punkt_odniesienia):
    plt.xlim(punkt_odniesienia.x-500, punkt_odniesienia.x+500)
    plt.ylim(punkt_odniesienia.y-500, punkt_odniesienia.y+500)
    plt.xlabel("OŚ X")
    plt.ylabel("OŚ Y")
    plt.title("Układ współrzędnych")
    plt.grid(True)
    plt.show()

def komunikat_postrzal(punkt_odniesienia):
    plt.text(punkt_odniesienia.x, punkt_odniesienia.y+250, "Trafiono w statek!")
