



def lista_contar():
    lista_vacia = []
    veces = int(input("Dime cuantos numeros quieres: "))
    cont = 0
    while cont < veces:
        numero = 1 + cont
        lista_vacia.append(numero)
        cont += 1
    return lista_vacia


print(lista_contar())