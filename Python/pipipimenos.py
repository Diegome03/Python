from cProfile import label
import math
from re import X
import matplotlib.pyplot as plt
from pyparsing import line 




puntos = range(1,12)
#logaritmo = [math.log(n) for n in puntos]
#linea =  [n for n in puntos]
loglinear = [n * math.log(n) for n in puntos]





ax = plt.subplot()



ax.plot(loglinear, label='Log Linear')
#ax.plot(linea, label='Lineal')
#ax.plot(logaritmo, label='Logaritmo')

plt.legend()
plt.ylabel('pasos')
plt.xlabel('tiempo')
plt.show()
