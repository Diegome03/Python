



listaciudades = ["Newyork", "Madrid", "Berlin"]
posiciones = [[10, 10], [30, 40], [18, 21]]
indices = list(range(len(listaciudades)))

posibilidades = []
def permutations(lista, final=[]):
    if len(lista) == 0:
        posibilidades.append(final)
    else:
        for i in range(len(lista)):
            permutations(lista[:i] + lista[i+1:], final + lista[i:i+1])


permutations(indices)
print("\nPermutacion de posiciones :")
print(posibilidades)
print("\nViajes posibles: ")
for posible_ruta in posibilidades:
    print("\n")
    for indice in posible_ruta:
        print(listaciudades[indice], end=" >> ")