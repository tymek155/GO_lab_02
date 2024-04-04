import Read

def main():
    r = Read.Read
    lista_punktow  = []
    lista_punktow, ilosc = r.read_file("dane.txt")
    print(ilosc)

if __name__ == '__main__':
    main()