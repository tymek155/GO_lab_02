import Read
import AlgorytmJarvisa

def main():
    r = Read.Read
    lista_punktow  = []
    lista_punktow, ilosc = r.read_file("test.txt")
    print(ilosc)
    algorytmJ = AlgorytmJarvisa.AlgorytmJarvisa()
    algorytmJ.otoczka(lista_punktow)

if __name__ == '__main__':
    main()