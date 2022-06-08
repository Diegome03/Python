import random

opciones = ["piedra", "papel", "tijeras"]
eleccioncpu = opciones[random.randint(0, len(opciones) - 1)]

victoriacpu = "Jeje, gané..."
derrotacpu = "¡ganaste!"
piedra_dibujo = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
papel_dibujo = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
tijeras_dibujo = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""


def obtener_jugada():
    apuesta = input("Escoge; piedra, papel o tijeras: ")

    while apuesta not in opciones:
        print("Por favor, escribe bien tu elección para poder jugar.")
        apuesta = input("Escoge; piedra, papel o tijeras: ")

    return apuesta


def jugador_eligio(player, jugada):
    if jugada == opciones[0]:
        print(f'{player} {opciones[0]}\n{piedra_dibujo}')
    elif jugada == opciones[1]:
        print(f'{player} {opciones[1]}\n{papel_dibujo}')
    elif jugada == opciones[2]:
        print(f'{player} {opciones[2]}\n{tijeras_dibujo}')


def juego():

    apuesta = obtener_jugada()

    # if apuesta == piedra:
    #     print(f'Tu escogiste {piedra}\n{piedra_dibujo}')
    # elif apuesta == papel:
    #     print(f'Tu escogiste {papel}\n{papel_dibujo}')
    # elif apuesta == tijeras:
    #     print(f'Tu escogiste {tijeras}\n{tijeras_dibujo}')
    # if eleccioncpu == piedra:
    #     print(f'Yo escogí piedra{piedra_dibujo}')
    # elif eleccioncpu == papel:
    #     print(f'Yo escogí papel{papel_dibujo}')
    # elif eleccioncpu == tijeras:
    #     print(f'Yo escogí tijeras{tijeras_dibujo}')
    #
    jugador_eligio("Tu escogiste", apuesta)
    jugador_eligio("la CPU eligió", eleccioncpu)

    if eleccioncpu == apuesta:
        print("Vaya, empatamos...")
    elif eleccioncpu == opciones[0] and apuesta == opciones[1]:
        print(derrotacpu)
    elif eleccioncpu == opciones[1] and apuesta == opciones[2]:
        print(derrotacpu)

    if eleccioncpu == opciones[2] and apuesta == opciones[0]:
        print(derrotacpu)
    elif eleccioncpu == opciones[0] and apuesta == opciones[2]:
        print(victoriacpu)
    elif eleccioncpu == opciones[1] and apuesta == opciones[0]:
        print(victoriacpu)

    if eleccioncpu == opciones[2] and apuesta == opciones[1]:
        print(victoriacpu)


def juego_infinito():
    juego()
    while True:
        if input("\n¿Quieres volver a jugar? [S/n]: \n").lower() == "s":
            juego()
        else:
            break


juego_infinito()
