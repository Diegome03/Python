import matplotlib.pyplot as plt

arr = [[6,6], [-1,8], [9,1], [6,-5]]

def coordenadas(lista):

    cont = 0

    while(cont < len(lista)-1):

        plt.xlim(-20, 20)
        plt.ylim(-20, 20)

        for coord in lista:
            x = lista[cont][0]
            y = lista[cont][1]
            cont += 1


            plt.scatter(x, y)
            plt.pause(0.30)


    plt.legend(lista)
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.show()







if __name__ == "main":
   print(f'mi nombres es >> {__name__}<<')

else:
    print (f'Importado como modulo: >>{__name__}<<')