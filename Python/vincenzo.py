from hashlib import new
from math import sqrt
import matplotlib.pyplot as plt

def plot_ruta(ruta,coordenadas_ciudades,best=False):
    x = []
    y = []
    for ciudad in ruta:
        x.append(coordenadas_ciudades[ciudad][0])
        y.append(coordenadas_ciudades[ciudad][1])
    if best:
        plt.plot(x,y,color='blue',marker='*',linewidth=3)
    else:
        plt.plot(x,y,color='gray',alpha=0.3,linewidth=1)

def distancia2ciudades(coor_ciudad1,coor_ciudad2):
    return sqrt((coor_ciudad1[0]-coor_ciudad2[0])**2+(coor_ciudad1[1]-coor_ciudad2[1])**2)

def distanciaruta(ruta,coordenadas_ciudades):
    distancia_total = 0.0
    #Reordenamos las coordenadas
    for ciudad in range(1,len(ruta)):
        ciudad_inicio = ruta[ciudad-1]
        ciudad_final  = ruta[ciudad]
        coordenadas_inicio = coordenadas_ciudades[ciudad_inicio]
        coordenadas_final = coordenadas_ciudades[ciudad_final]
        distancia_parcial = distancia2ciudades(coordenadas_inicio,coordenadas_final)
        distancia_total = distancia_total + distancia_parcial
    return distancia_total

# Implementa el metodo de Heap para permutar listas
def PermutaCiudades(ciudades, size, combinaciones=[]):
    # Si la dimension de la lista es 1, agrega la permutacion a la lista
    if size == 1:
        #print(ciudades)
        combinaciones.append(ciudades[:])
        return combinaciones

    for i in range(size):
        PermutaCiudades(ciudades, size - 1)

        # Si size es par alterna el elemento actual con el ultimo elemento (i, size-1)
        if (size % 2) == 0:
            ciudades[i], ciudades[size - 1] = ciudades[size - 1], ciudades[i]
        # Si size es impar alterna el primer elemento con el ultimo elemento (0, size-1)
        else:
            ciudades[0], ciudades[size - 1] = ciudades[size - 1], ciudades[0]

    return combinaciones

def ind_distancia(ruta):
    return ruta[-1]

if __name__=="__main__":
    #####  Parametros del condigo, Ciudades y cordenadas ##########
    nombre_ciudades = ['NewYork','Madrid','Lisboa','Berlin','Paris']
    coordenadas_ciudades = [(0,70),(40,30),(30,25),(80,55),(60,40)]
    ###############################################################

    # n es el numero de ciudades
    n = len(nombre_ciudades)
    # Asigno un indice a cada ciudad (desde cero al numero de ciudades)
    id_ciudades=[]
    for id in range(n):
        id_ciudades.append(id)
    # Ejemplo Distancia entre dos ciudades
    # Distancia entre New York y Lisboa
    print(f'Las coordenadas de NewYork son: {coordenadas_ciudades[0]}')
    print(f'Las coordenadas de Lisboa son: {coordenadas_ciudades[2]}')
    distancia_Lisboa_NY = distancia2ciudades(coordenadas_ciudades[0],coordenadas_ciudades[2])
    print(f'La distancia entre las dos ciudades es: {distancia_Lisboa_NY}')

    # Distancia de Ruta
    # Calcular la distancia total de una ruta determinada
    # RUTA:  ['NewYork','Madrid'','Berlin','Lisboa]
    newyork = 0
    madrid = 1
    berlin = 2
    lisboa = 3
    paris = 4
    ruta=[newyork,berlin,madrid,paris]
    print(f'La ruta seleccionada es: {ruta}')
    distancia_total_ruta=distanciaruta(ruta,coordenadas_ciudades)
    print(f'La distancia total es: {distancia_total_ruta}')


    # cada ruta es una lista de indice de ciudades
    # rutas es una lista de rutas (lista de listas)
    rutas = PermutaCiudades(id_ciudades, n)

    # Para cada ruta calculamos la distancia
    # cada ruta_con_distancia es una lista con el ultimo elemento la distancia de la ruta
    rutas_con_distancias = []
    rutas_id_con_distancias = []
    for ruta in rutas:
        # En esta funcion se calcula la distanca de toda la ruta (internamente calcula la distancia entre las ciudades0
        distancia_ruta = distanciaruta(ruta,coordenadas_ciudades)
        ruta_con_distancia = []
        ruta_id_con_distancia = []
        for ciudad in ruta:
            ruta_con_distancia.append(nombre_ciudades[ciudad])            
        ruta_con_distancia.append(distancia_ruta)
        ruta.append(distancia_ruta)
        rutas_con_distancias.append(ruta_con_distancia)
        rutas_id_con_distancias.append(ruta)

    #Ordenar basado en la funcion ind_distancia
    rutas_con_distancias.sort(key=ind_distancia)
    rutas_id_con_distancias.sort(key=ind_distancia)

    for ruta in rutas_con_distancias:
        print(ruta)
    for ruta in rutas_id_con_distancias:
    
        # para Graficar todas las rutas
        plot_ruta(ruta[:n],coordenadas_ciudades)
    # Graficar la mejor ruta
    plot_ruta(rutas_id_con_distancias[0][:n],coordenadas_ciudades,best=True)
    # Pone las coordenadas y nombres de las ciudades
    for ciudad,coordenada in zip(nombre_ciudades,coordenadas_ciudades):
        plt.annotate(f"{ciudad}: {coordenada}",coordenada)

    plt.show()



