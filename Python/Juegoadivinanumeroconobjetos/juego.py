from random import randint
from usuario import Usuario


class Juego:

    num = None
    usuario = None

    def __init__(self):
        self.num = randint(1, 10)
        self.usuario = Usuario()

    def juega(self):

        while(self.usuario.num != self.num):
            self.usuario.introducirNum()
            if self.num < self.usuario.num:
                print(f'El numeroque buscas es mas pequeño (pista:)')
            elif self.num > self.usuario.num:
                print(f'El numeroque buscas es mas grande (pista:)')
            else:
                self.victoria()


    def victoria(self):
        print("Has ganado")
