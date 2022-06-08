




numeros = [4, 8, 78, 99, 37, 54, -99, 3, -987987987, 989898, 7 ]
cositi = [5, 44, 95, 1 , 0 , -5]
aaaaaa = [99, 55, 77, -8, -9, -100, 0]
nueva_lista = []



def ordenararray(lista):
    print(f'Lista original \n{lista}\n')
    while(len(lista)):
        minimo = min(lista)
        nueva_lista.append(minimo)
        indice = lista.index(minimo)
        lista.pop(indice)
    return nueva_lista



print(f'Lista ordenada de menor a mayor \n{ordenararray(cositi)}\n')




