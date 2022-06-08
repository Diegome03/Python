

from tkinter import N
from unicodedata import numeric


numero = int(input("Introduce numero fibonacci: "))
rango = range(1,10)





def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n-1) + fib(n-2)


print(fib(numero))



"""
if __name__ == '__main__':
    fibonacci = fib(10)
    print('Fibonacci de orden 10:')
    print(fibonacci)
"""



