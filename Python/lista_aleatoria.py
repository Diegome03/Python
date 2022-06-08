import random


def lista_rango_0_a_100():
    lista_vacia = []
    veces = int(input("Dime cuantos numeros aleatorios quieres(rango entre 0 y 100): "))
    cont = 0
    while cont < veces:
        numero = random.randint(0, 100)
        lista_vacia.append(numero)
        cont += 1
    return lista_vacia


print(lista_rango_0_a_100())
