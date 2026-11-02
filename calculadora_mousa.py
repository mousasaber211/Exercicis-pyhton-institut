
funcionar = True
print('BIENVENIDO A LA CALCULADORA')

while funcionar:
    print('MENÚ DE OPERACIONES')
    print('1 - SUMAR')
    print('2 - RESTAR')
    print('3 - MULTIPLICAR')
    print('4 - DIVIDIR')
    print('5 - ÁREA DE UN CUADRADO')
    print('6 - ECUACIÓN DE PRIMER GRADO')
    print('7 - POTENCIAS')
    print('8 - RAÍZ CUADRADA')
    print('9 - ÁREA DE UN CÍRCULO')
    print('10 - ÁREA DE UN TRIÁNGULO')
    print('0 - SALIR')

    operacion = input('Elija la opción que desee:')

    if operacion == '1':
        numero1 = float(input('Introduzca el primer número:'))
        numero2 = float(input('Introduzca el segundo número:'))
        print('Resultado:', numero1 + numero2)

    elif operacion == '2':
        numero1 = float(input('Introduzca el primer número:'))
        numero2 = float(input('Introduzca el segundo número:'))
        print('Resultado:', numero1 - numero2)

    elif operacion == '3':
        numero1 = float(input('Introduzca el primer número:'))
        numero2 = float(input('Introduzca el segundo número:'))
        print('Resultado:', numero1 * numero2)

    elif operacion == '4':
        dividendo = float(input('Introduzca el dividendo:'))
        divisor = float(input('Introduzca el divisor:'))

        if divisor == 0:
            print('ERROR: No se puede dividir entre 0.')
        else:
            print('Resultado:', dividendo / divisor)

    elif operacion == '5':
        lado = float(input('Introduzca el lado del cuadrado:'))
        print('Área:', lado * lado)

    elif operacion == '6':
        print('Introduzca una ecuación tipo ax + b = 0.')
        a = float(input('Introduzca el valor de a:'))
        b = float(input('Introduzca el valor de b:'))

        if a == 0:
            if b == 0:
                print('La ecuación tiene infinitas soluciones.')
            else:
                print('La ecuación no tiene solución.')
        else:
            resultado = -b / a
            print('Solución: x =', resultado)

    elif operacion == '7':
        base = float(input('Introduzca la base:'))
        exponente = float(input('Introduzca el exponente:'))

        if base == 0 and exponente < 0:
            print('ERROR: No se puede dividir entre 0.')
        else:
            print('Resultado:', base ** exponente)

    elif operacion == '8':
        numero = float(input('Introduzca el número: '))

        if numero < 0:
            print('ERROR: No existe raíz cuadrada real de un número negativo.')
        else:
            print('Resultado:', numero ** 0.5)

    elif operacion == '9':
        radi = float(input('Introduzca el radi del círculo:'))

        if radi < 0:
            print('ERROR: El radi no puede ser negativo.')
        else:
            area = 3.14 * radi ** 2
            print('Área:', area)

    elif operacion == '10':
        base = float(input('Introduzca la base del triángulo:'))
        altura = float(input('Introduzca la altura del triángulo:'))

        if base < 0 or altura < 0:
            print('ERROR: Las medidas no pueden ser negativas.')
        else:
            area = base * altura / 2
            print('Área:', area)

    elif operacion == '0':
        funcionar = False

    else:
        print('ERROR: Opción no válida.')

    if funcionar:
        respuesta = input('Quieres realizar otro cálculo? (si/no):')
        respuesta = respuesta.lower()

        if respuesta == 'si':
            funcionar = True
        else:
            funcionar = False

print('Saliendo de la calculadora...')

print('Calculadora cerrada con éxito.')

