funcionar = True
print('BIENVENIDO A LA CALCULADORA')

while funcionar == True:

    print('Menú de operaciones:')
    print('1-SUMAR')
    print('2-RESTAR')
    print('3-MULTIPLICAR')
    print('4-DIVIDIR')
    print('5-AREA DE UN CUADRADO')
    print('6-EQUACION 1r GRADO')

    operacion = input('Elija el numero de la operación que quiera realizar:')

    if operacion == 1:
        numero1 = float(input('Introduzca el primer numero'))
        numero2 = float(input('Introduzca el segundo numero'))
        print('Resultado:', numero1 + nuemro2)

    elif operacion == 2:
        numero1 = float(input('Introduzca el primer numero'))
        numero2 = float(input('Introduzca el segundo numero'))
        print('Resultado:', numero1 - numero2)

    elif operacion == 3:
        numero1 = float(input('Introduzca el primer numero'))
        numero2 = float(input('Introduzca el segundo numero'))
        print('Resultado:', numero1 * numero2)

    elif operacion == 4:
        dividiendo = float(input('Introduzca el dividiendo'))
        divisor = float(input('Introduzca el divisor'))
        if divisor == 0:
            print('ERROR -> No se puede dividir entre 0')
        else:
            print('Resultado:', dividiendo / divisor)

    elif operacion == 5:
        lado = float(input('Introduzca el lado del cuadrado:'))
        print('Resultado:', lado * lado)

    elif operacion == 6:
        print('Introduzca una equacion tipo -> ax + b = 0:')
        a = float(input('Introduzca la (a) con su signo:'))
        b = float(input('introduzca la (b) con su signo:'))
        if a == 0:

        resultado = -b / a 
        print(resultado)


    




 

  
