

print("__________________________________________________________________________")

numeros = [0,25,0,50,0,75,0,100,0,125,0,150]

print(f'\nLista original\n{numeros}\n')

def revertir(lista):
    nueva_lista = []
    for elemento in lista[::-1]:
        nueva_lista.append(elemento)
    print(f'Revertir hecho a mano \n{nueva_lista}\n')
    return nueva_lista

def exponente(lista):
    nueva_lista = []
    print("Exponente con for")

    for elemento in lista:
        cuadrado = elemento ** 2
        nueva_lista.append(cuadrado)
    print(nueva_lista)
    print()
    return nueva_lista

def limpiar(lista):
    nueva_lista = []
    for elemento in lista:
        numeros = nueva_lista
    print(f'Clear \n{numeros}\n')

    return nueva_lista

def quitarceros(lista):
    nueva_lista = []
    for elemento in lista:
        if (elemento != 0):
            nueva_lista.append(elemento)
    print(nueva_lista)
    return nueva_lista

revertir(numeros)
exponente(numeros)
limpiar(numeros)
quitarceros(numeros)

print("___________________________________________________________________________")
