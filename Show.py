import matplotlib.pyplot as plt

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
