

from cProfile import label
import math
from re import X
import matplotlib.pyplot as plt 


puntos = range(1, 5)
linea =  [n for n in puntos]
factorial =  [math.factorial(n) for n in puntos]
exponencial =  [2**n for n in puntos]
cuadrado = [n**2 for n in puntos]
cubo = [n**3 for n in puntos]
constante = [1 for n in puntos]  #4
logaritmo = [math.log(n) for n in puntos]
loglinear = [n * math.log(n) for n in puntos]


ax = plt.subplot()


ax.plot(linea, label='n')
ax.plot(constante, label='Constante')
ax.plot(cuadrado, label='Al cuadrado')
ax.plot(cubo, label='Al cubo')
ax.plot(exponencial, label='Exponencial')
ax.plot(factorial, label='Factorial')
ax.plot(logaritmo, label='Logaritmo')
ax.plot(loglinear, label='Log linear')




plt.legend()
plt.ylabel('pasos')
plt.xlabel('tiempo')
plt.show()

'''
def loga(puntos):
    logaritmo = []
    for n in puntos:
        if n == 0:
            logaritmo.append(None)
        else:
            logaritmo.append(math.log(n))

    return logaritmo
'''