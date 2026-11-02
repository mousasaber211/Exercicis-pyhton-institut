
import random

jugar = True

print('BIENVENIDO AL JUEGO DE ADIVINAR EL NÚMERO')

while jugar == True:

    numero_secreto = random.randint(1, 100)
    intentos = 0
    acertado = False

    print('El juego ha pensado un número entre 1 y 100.')
    print('Intenta adivinarlo!')

    while acertado == False:

        numero = int(input('Introduce un numero:'))
        intentos += 1

        if numero < numero_secreto:
            print('El número secreto es MAYOR.')

        elif numero > numero_secreto:
            print('El número secreto es MENOR.')

        else:
            acertado = True
            print('FELICIDADES! Has acertado.')
            print('El número era:', numero_secreto)
            print('Número de intentos:', intentos)

    respuesta = input('Quieres jugar otra partida? (si/no): ')
    respuesta = respuesta.lower()

    if respuesta == 'si':
        jugar = True
    else:
        jugar = False

print('Saliendo del juego...')
print('Juego cerrado con exito.')
