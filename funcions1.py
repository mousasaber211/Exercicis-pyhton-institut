terminamos = 0 #Creamos una variable de control
def funcionSuma (): #Creamos la función
    numero1 = input ("Primer número: ") #Pedimos los números a sumar
    numero2 = input("Segundo número: ")

    numero1 = int (numero1) #Los convertimos en enteros
    numero2 = int (numero2)

    suma = numero1 + numero2 #Sumamos e imprimimos los números
    print (suma)

while terminamos == 0: #Creamos un bucle y mostramos opciones
    print ( "Nuestras opciones:")
    print ( "1. Realizar una suma")
    print ( "2. Terminar")

    pregunta = input ( "¿Qué quieres hacer? (1 o 2): ") #Preguntamos

    if pregunta == "1":
        funcionSuma () #Llamamos a la función
    elif pregunta == "2":
        print ( "Adiós")
        terminamos = 1 #Opción para terminar el bucle