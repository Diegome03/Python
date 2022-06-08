
from ast import Return
from email.errors import InvalidMultipartContentTransferEncodingDefect
from math import dist


listaciudades = ["Newyork", "Madrid", "Berlin"]
posiciones = [[10, 10], [30, 40], [18, 21]]
indices = list(range(len(listaciudades)))

distancia1 = dist(posiciones[0], posiciones[1])
distancia2 = dist(posiciones[1], posiciones[2])
distancia = distancia1 + distancia2


posibilidades = []


def permutations(lista, final=[]):
    if len(lista) == 0:
        posibilidades.append(final)
    else:
        for i in range(len(lista)):
            permutations(lista[:i] + lista[i+1:], final + lista[i:i+1])


permutations(indices)

print(posibilidades)


def viajes(x):
    for posible_ruta in posibilidades:
        print(f'  {distancia}')
        for indice in posible_ruta:
            print(x[indice], end=" >> ")


viajes(listaciudades)


# for posible_ruta in posibilidades:
# print("\n")
# for indice in posible_ruta:
#print(posiciones[indice], end=" >> ")
