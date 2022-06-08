import random


intentosRealizados = 0

print("\n¡Hola!¿Cómo te llamas?")
miNombre = input()
print(f'\n¡Bienvenido {miNombre}!\n¿Jugamos a un juego? Dame dos numeros para establacer un rango en el que yo escoja un numero al azar y tu tengas que adivinarlo...\n')
numrango1 = int(input("Dime el primer numero que quieres del rango: "))
numrango2 = int(input("Dime el segundo numero que quieres del rango: "))
print()
número = random.randint(numrango1,numrango2)



print(f'Bien, {miNombre}, entonces tendras que adivinar un numero entre {numrango1} y {numrango2}.\n')

numintentos = int(input("¿En cuantos intentos crees que eres capaz de hacerlo?: "))
print()
print(f'De acuerdo, entonces tendras {numintentos} intentos para adivinarlo, mucha suerte.')
if numrango1 == 7:
    print("PISTA:(Puede que este pensando en el agente James Bond...)\n")

while intentosRealizados < numintentos:
    print('Intenta adivinar: ') # Hay cuatro espacios delante de print.

    estimación = input()

    estimación = int(estimación)

    intentosRealizados = intentosRealizados + 1

    if estimación < número:

        print('Tu estimación es mas baja.') # Hay ocho espacios delante de print.

    if estimación > número:

        print('Tu estimación es mas alta.')


    if estimación == número:
        break

if estimación == número:

    intentosRealizados = str(intentosRealizados)

    print(f'''¡Buen trabajo, {miNombre}! ¡Has adivinado mi número en {intentosRealizados} intentos!

                    ░░░░░░░░░░░░░░░░░░░░░░█████████
                    ░░███████░░░░░░░░░░███▒▒▒▒▒▒▒▒███
                    ░░█▒▒▒▒▒▒█░░░░░░░███▒▒▒▒▒▒▒▒▒▒▒▒▒███
                    ░░░█▒▒▒▒▒▒█░░░░██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██
                    ░░░░█▒▒▒▒▒█░░░██▒▒▒▒▒██▒▒▒▒▒▒██▒▒▒▒▒███
                    ░░░░░█▒▒▒█░░░█▒▒▒▒▒▒████▒▒▒▒████▒▒▒▒▒▒██
                    ░░░█████████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██
                    ░░░█▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒██
                    ░██▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒██▒▒▒▒▒▒▒▒▒▒██▒▒▒▒██
                    ██▒▒▒███████████▒▒▒▒▒██▒▒▒▒▒▒▒▒██▒▒▒▒▒██
                    █▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒████████▒▒▒▒▒▒▒██
                    ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██
                    ░█▒▒▒███████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██
                    ░██▒▒▒▒▒▒▒▒▒▒████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█
                    ░░████████████░░░█████████████████
''')


if estimación != número:

    número = str(número)

    print(f'''Superaste los {numintentos} intentos que te propusiste... El número que estaba pensando era {número}
    
                                ───────────────────██
                                ──────────────────█─██
                                ──────────────────█───█
                                ──────────────────█───█
                                ──────────────────█───█
                                ──────────────────█───█
                                ──────────────────█───█▓
                                ──────────────────█───▓█
                                ──────────────────█───░█
                                ──────────────────█───░█
                                ──────────────────█░░░─█
                                ───────────▓███──██▓▓███
                                ───────────██──▓██▓────██
                                ───────────█▓────█▓─────▓█
                                ───────────█▓─────█──────░█
                                ██████─────█▓─────█────────█
                                ████████▓███░──────█──█▓────█
                                █░░░░░░█───────────█░███────█▓
                                ▓██████─────────────█▓██────██
                                ███████░────────────────────▓█
                                ▓██████░────────────────────░█
                                ▓██████░────────────────────▓█
                                ▓██████░────────────────────█▓
                                ▓██████░────────────────────█
                                ▓██████░───────────────────██
                                ▓███░██░──────────────────█
                                ▓███──████████████████████
                                ██████
    
''')