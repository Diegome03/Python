
class Casilla:

    def __init__(self, number):
        self.number = number
        self.is_water = True
        self.hitted = False
    
    def is_ship(self):
        return not self.is_water

    def dispara(self):
        if (self.is_ship()):
            self.hitted = True

    def __str__(self):
        posicion = {self.number}
        txt = ' ' + f"".rjust(1) +'▄' if not self.hitted else 'X'
        return txt 
class Tablero:
    def __init__(self):
        self.num_filas = 10
        self.num_columnas = 10
        self.casillas = []
        for i in range(self.num_filas * self.num_columnas):
            self.casillas.append(Casilla(i))

    def mostrar(self):
        for fila in range(self.num_filas):
            print(end="\n")
            for col in range(self.num_columnas):
                i = fila * 10 + col
                casilla = self.casillas[i]
                print(casilla, end="")




        # # Aquí te dibuja el tablero
        # self.num_filas = 10
        # self.num_columnas = 10
        # self.contador = 0
        # self.contador2 = 0
        # self.abecedario = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k",
        #                    "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        # self.letra = (f' {self.abecedario[self.contador2]}')
        # self.casillas_top = "---+"
        # self.casillas_lados = "   |"
        # print("Hola")
        # while self.contador2 < self.num_columnas:
        #     self.contador2 += 1

        # print("   " + self.letra * self.num_columnas)

        # while self.contador < self.num_filas:
        #     print("  +"+self.casillas_top * self.num_columnas)
        #     print(str(self.contador) + " |" +
        #           self.casillas_lados * self.num_columnas)
        #     self.contador += 1

        # print("  +"+self.casillas_top * self.num_columnas)


xtablero = Tablero()
xtablero.mostrar()
