import Read
import AlgorytmJarvisa
from Show import wyswietl_punkty, wyswietl_punkty_short
from AlgorytmJarvisa2 import gift_wrapping

def main():
    r = Read.Read
    lista_punktow  = []
    lista_punktow, ilosc = r.read_file("dane2.txt")
    print(ilosc)
    #wyswietl_punkty(lista_punktow)
    algorytmJ = AlgorytmJarvisa.AlgorytmJarvisa()
    lewa, prawa = algorytmJ.otoczka(lista_punktow)
    punkty = gift_wrapping(lista_punktow)
    wyswietl_punkty_short(lewa)
    wyswietl_punkty(prawa)
    wyswietl_punkty(punkty)

if __name__ == '__main__':
    main()