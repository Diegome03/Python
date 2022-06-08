


def funcion(lista):
    nueva_lista = []


    for elemento in lista[::-1]:
        nueva_lista.append(elemento)

    for elemento in lista:
        if (elemento != 0):
            nueva_lista.append(elemento)

    for elemento in lista:
        cuadrado = elemento ** 2
        nueva_lista.append(cuadrado)

        return nueva_lista


