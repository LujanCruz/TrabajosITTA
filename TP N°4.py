#1)Escriba una función que muestre todos los números primos entre 1 y un número n que es
#ingresado por parámetro.

#def es_primo(num):
#    if num < 2:
#        return False
#    for i in range(2, int(num**0.5) + 1):
#        if num % i == 0:
#            return False
#    return True

#def numeros_primos_hasta_n(n):
#    primos = []
#   for num in range(2, n + 1):
#        if es_primo(num):
#            primos.append(num)
#    return primos

#try:
#    n = int(input("Ingrese un número entero mayor que 1: "))
#    if n <= 1:
#        raise ValueError
#except ValueError:
#    print("Ingrese un número entero mayor que 1.")
#else:
#    primos = numeros_primos_hasta_n(n)
#    print("Números primos hasta", n, ":", primos)

#2) Escriba una función que le pida al usuario ingresar condimentos para un sándwich, hasta
#que el usuario ingrese ‘salir’. Cada vez que se ingrese un condimento, muestre un mensaje
#avisando que ya se agregó el condimento al sándwich. Escriba versiones diferentes del
#programa de acuerdo a estos criterios:
#• Use un test condicional en el ciclo while para detener la ejecución.
#• Use un test condicional dentro del ciclo para decidir si continuar la ejecución. 


#Version de test condicional en el ciclo while para detener la ejecución.
#def armar_sandwich():
#    condimentos = []
#    condimento = input("Ingrese un condimento para el sándwich (o 'salir' para terminar): ")
#
#    while condimento.lower() != 'salir':
#        condimentos.append(condimento)
#        print(f"Se ha agregado '{condimento}' al sándwich.")
#        condimento = input("Ingrese otro condimento (o 'salir' para terminar): ")
#
#    print("\nCondimentos en el sándwich:")
#    for cond in condimentos:
#        print("- " + cond)

#if __name__ == "__main__":
#    armar_sandwich()

#Version de test condicional dentro del ciclo para decidir si continuar la ejecución.
#def armar_sandwich():
#    condimentos = []
#
#    while True:
#        condimento = input("Ingrese un condimento para el sándwich (o 'salir' para terminar): ")
#
#        if condimento.lower() == 'salir':
#            break
#
#        condimentos.append(condimento)
#        print(f"Se ha agregado '{condimento}' al sándwich.")
#
#    print("\nCondimentos en el sándwich:")
#    for cond in condimentos:
#        print("- " + cond)
#
#if __name__ == "__main__":
#    armar_sandwich()

#3) A) Remera: Escriba una función “hacer_remera()” que tome como parámetros un
#tamaño y el mensaje que debería ir impreso en la remera. La función debe mostrar un mensaje
#describiendo el tamaño de la remera y el mensaje impreso en ella. Llame la función una vez
#usando argumentos por posición. Llámela una segunda vez usando argumentos por clave.



#B) Remeras Grandes: Modifique la “funcion hacer_remera()” para que el tamaño por
#defecto sea ‘L’ y el mensaje, ‘Me gusta Python’. Haga un par de remeras, la primera con los
#valores por defecto, y la segunda con valores diferentes. 



#4) Serie de Fibonacci: Escriba una función fibonacci(n) que devuelva los n primeros numeros 
#de la serie de Fibonacci. En esta serie, los primeros dos números son 0 y 1, y cada sucesivo 
#número es la suma de los dos números inmediatamente anteriores (ejemplo: 0,1,1,2,3,5,8, …).

#def Fibonacci(n):

#    if n <= 0:
#        raise ValueError("El valor de n debe ser mayor que cero.")

#    fib_sequence = [0, 1]

#    for i in range(2, n):
#        next_number = fib_sequence[-1] + fib_sequence[-2]
#        fib_sequence.append(next_number)

#    return fib_sequence

#n = 10
#result = Fibonacci(n)
#print(result)

#6) (Opcional) Conversión imperial: Desarrollar un programa en Python que pueda convertir 
#gramos a libras, centímetros a pulgadas y kilómetros a millas. El programa debe permitir la 
#conversión en ambos sentidos. 1.60934 Km = 1 milla 0.393701 pulgadas = 1 cm 0.00220462 
#libras = 1 gramo

def gramos_a_libras(gramos):
    return gramos * 0.00220462

def libras_a_gramos(libras):
    return libras / 0.00220462

def centimetros_a_pulgadas(centimetros):
    return centimetros * 0.393701

def pulgadas_a_centimetros(pulgadas):
    return pulgadas / 0.393701

def kilometros_a_millas(kilometros):
    return kilometros / 1.60934

def millas_a_kilometros(millas):
    return millas * 1.60934

#opciones
def mostrar_menu():
    print("Seleccione una opción:")
    print("1. Gramos a Libras")
    print("2. Libras a Gramos")
    print("3. Centímetros a Pulgadas")
    print("4. Pulgadas a Centímetros")
    print("5. Kilómetros a Millas")
    print("6. Millas a Kilómetros")
    print("0. Salir")

# Programa principal
while True:
    mostrar_menu()
    opcion = int(input("Opción: "))

    if opcion == 0:
        print("¡Hasta luego!")
        break

    elif opcion == 1:
        gramos = float(input("Ingrese la cantidad en gramos: "))
        libras = gramos_a_libras(gramos)
        print(f"{gramos} gramos = {libras:.4f} libras")

    elif opcion == 2:
        libras = float(input("Ingrese la cantidad en libras: "))
        gramos = libras_a_gramos(libras)
        print(f"{libras} libras = {gramos:.4f} gramos")

    elif opcion == 3:
        centimetros = float(input("Ingrese la cantidad en centímetros: "))
        pulgadas = centimetros_a_pulgadas(centimetros)
        print(f"{centimetros} centímetros = {pulgadas:.4f} pulgadas")

    elif opcion == 4:
        pulgadas = float(input("Ingrese la cantidad en pulgadas: "))
        centimetros = pulgadas_a_centimetros(pulgadas)
        print(f"{pulgadas} pulgadas = {centimetros:.4f} centímetros")

    elif opcion == 5:
        kilometros = float(input("Ingrese la cantidad en kilómetros: "))
        millas = kilometros_a_millas(kilometros)
        print(f"{kilometros} kilómetros = {millas:.4f} millas")

    elif opcion == 6:
        millas = float(input("Ingrese la cantidad en millas: "))
        kilometros = millas_a_kilometros(millas)
        print(f"{millas} millas = {kilometros:.4f} kilómetros")

    else:
        print("Opción inválida. Intente nuevamente.")