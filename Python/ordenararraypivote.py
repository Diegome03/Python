

from re import A


array = [69, 92, 27, 5, 47, 61, 16, 38, 2]
newarray = []




medio = len(array) /2
posicionmedio = array[int(medio)]
indice = array.index(posicionmedio)
minimoizq = min(array[:indice])
indicemedio = array.index(minimoizq)
cogerpequeñoizquierda = array.pop(indicemedio)
añadiralprincipio = newarray.append(cogerpequeñoizquierda)
print(minimoizq)
