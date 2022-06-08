


numero = 2

def par_impar(x):
    if type(x) != int:
        return None
    if (x % 2) == 0:
        return True
    else:
        return False

if par_impar(numero) == None:
    print("No has introducido un valor entero")
elif par_impar(numero) == True:
    print("Es par")
elif par_impar(numero) == None:
    print("Es impar")


