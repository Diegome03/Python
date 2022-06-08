import coordenadas_min_max
import random
import math

shots = 12
lista_shots = [[0, 0], [0.2, 0.3], [-0.4, 0.6], [1, 1.1], [-0.9, 2], [0-2, 3.3], [-0.7, 6.8], [-1, 7.1] , [-1.3,6]]



def hipotenusa(lista):
    lista_hipotenusa = []
    for x in lista:
        hipo = math.sqrt((x[0]**2) + (x[1]**2))
        lista_hipotenusa.append(hipo)

    return lista_hipotenusa


def azar(lista):
    list_shots_azar = []
    cont = 0

    while(cont < len(lista)):
        rand_rango = random.uniform(hipotenusa(lista_shots)[cont]*-1, hipotenusa(lista_shots)[cont])
        list_shots_azar.append(rand_rango)
        cont += 1
    return list_shots_azar


def sumar_aleatorio_x_y(lista):
    lista_shots_aleatorios = []
    cont = 0
    while(cont < len(lista)-1):
        lista_x_y = []
        lista_x_y.append(lista_shots[cont][0] + azar(lista_shots)[cont])
        lista_x_y.append(lista_shots[cont][1] + azar(lista_shots)[cont])
        cont += 1
        lista_shots_aleatorios.append(lista_x_y)
    return lista_shots_aleatorios


print(sumar_aleatorio_x_y(lista_shots))

coordenadas_min_max.punto_de_mira(sumar_aleatorio_x_y(lista_shots))
