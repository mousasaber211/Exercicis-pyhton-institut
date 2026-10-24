funcionar = True
print('BIENVENIDO A LA CALCULADORA')

while funcionar:
    print('Menú de operaciones:')
    print('1 - SUMAR')
    print('2 - RESTAR')
    print('3 - MULTIPLICAR')
    print('4 - DIVIDIR')
    print('5 - ÁREA DE UN CUADRADO')
    print('6 - ECUACIÓN DE PRIMER GRADO')
    print('7 - SALIR')

    operacion = input('Elija la opciónm que desee: ')

    if operacion == '1':
        numero1 = float(input('Introduzca el primer número: '))
        numero2 = float(input('Introduzca el segundo número: '))
        print('Resultado:', numero1 + numero2)

    elif operacion == '2':
        numero1 = float(input('Introduzca el primer número: '))
        numero2 = float(input('Introduzca el segundo número: '))
        print('Resultado:', numero1 - numero2)

    elif operacion == '3':
        numero1 = float(input('Introduzca el primer número: '))
        numero2 = float(input('Introduzca el segundo número: '))
        print('Resultado:', numero1 * numero2)

    elif operacion == '4':
        dividendo = float(input('Introduzca el dividendo: '))
        divisor = float(input('Introduzca el divisor: '))

        if divisor == 0:
            print('ERROR: No se puede dividir entre 0.')
        else:
            print('Resultado:', round(dividendo / divisor))

    elif operacion == '5':
        lado = float(input('Introduzca el lado del cuadrado: '))
        print('Área:', lado * lado)

    elif operacion == '6':
        print('Introduzca una ecuación tipo ax + b = 0.')
        a = float(input('Introduzca el valor de a: '))
        b = float(input('Introduzca el valor de b: '))

        if a == 0:
            if b == 0:
                print('La ecuación tiene infinitas soluciones.')
            else:
                print('La ecuación no tiene solución.')
        else:
            resultado = -b / a
            print('Solución: x =', resultado)

    elif operacion == '7':
        funcionar = False
        print('Saliendo del programa...')

    else:
        print('Opción no valida. Elija un numero del 1 al 7.')
    