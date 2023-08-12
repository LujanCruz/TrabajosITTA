#1. Escriba una función redondear() que permita redondear un número
#decimal de acuerdo al criterio: Si el número es mayor a 3.50, devolver el
#entero siguiente (en este caso, 4), si no devolver el entero inmediatamente
#anterior (3). 

#def redondear(numero):
#    entero_parte = int(numero)
#    decimal_parte = numero - entero_parte
#
#    if decimal_parte > 0.50:
#        return entero_parte + 1
#    else:
#        return entero_parte

#try:
#    numero_str = input("Ingresa un número decimal: ")
#    numero = float(numero_str)

#    resultado = redondear(numero)

#    print("El redondeo del número ingresado es:", resultado)

#except ValueError:
#    print("Error: Por favor, ingresa un número decimal válido.")

#2. Coloque el módulo del ejercicio anterior dentro de un paquete. En un
#módulo que esté fuera de ese paquete, cree una función de suma de
#decimales que redondee el resultado haciendo uso de la función
#redondear() del paquete recién creado.

#3. Usando el módulo datetime, escribe un programa que muestre la fecha 
#y hora actuales del sistema.

#import datetime

#fecha_hora_actual = datetime.datetime.now()
#formato = "%Y-%m-%d %H:%M:%S"
#fecha_hora_formateada = fecha_hora_actual.strftime(formato)
#print("La fecha y hora actuales son:", fecha_hora_formateada)

#4. Escriba un programa que devuelva un número par al azar entre 2 y 10
#(pista: para comprobar si se pueden generar todos los números, pruebe
#ejecutar el programa dentro de un ciclo infinito).

#import random

#def generar_numero_par():
#    return random.randrange(2, 11, 2)

#numero_par = generar_numero_par()
#print("Número par generado:", numero_par)


#5. Bola mágica: La bola mágica (Magic 8 ball) es un popular juguete usado
#para la adivinación o para buscar consejo. Su mecanismo es muy simple:
#ante una pregunta del usuario, la bola responde con una de 8 posibles
#respuestas:
#- Es seguro que sí
#- Las chances son buenas
#- Puedes contar con ello
#- Pregúntame de nuevo más tarde
#- Concéntrate y pregunta de nuevo
#- No veo con claridad, intenta de nuevo
#- Mi respuesta es no
#- Mis fuentes me dicen que no
#Escriba una función en Python para simular la bola mágica.

#import random

#def bola_magica():
#    respuestas = [
#        "Es seguro que sí",
#        "Las chances son buenas",
#        "Puedes contar con ello",
#        "Pregúntame de nuevo más tarde",
#        "Concéntrate y pregunta de nuevo",
#        "No veo con claridad, intenta de nuevo",
#        "Mi respuesta es no",
#        "Mis fuentes me dicen que no"
#    ]
#    return random.choice(respuestas)

#pregunta = input("Hazme una pregunta: ")
#respuesta = bola_magica()
#print("La bola mágica dice:", respuesta)

#6. Encuentre el tiempo de ejecución de los programas de los ejercicios 
#anteriores (pista: use el módulo time)

#7. (Opcional) Sorteo: Escriba un programa que simule un sorteo donde
#toman uno o más papeles al azar de un pozo para elegir los ganadores.

import random

def sorteo(participantes, num_ganadores):
    if num_ganadores > len(participantes):
        return "No hay suficientes participantes para elegir tantos ganadores."

    ganadores = random.sample(participantes, num_ganadores)
    return ganadores

try:
    num_participantes = int(input("Ingresa el número de participantes: "))
    participantes = []

    for i in range(num_participantes):
        participante = input(f"Ingresa el nombre del participante {i + 1}: ")
        participantes.append(participante)

    num_ganadores = int(input("Ingresa el número de ganadores: "))

    resultados = sorteo(participantes, num_ganadores)

    if isinstance(resultados, str):
        print(resultados)
    else:
        print("Los ganadores del sorteo son:")
        for i, ganador in enumerate(resultados, start=1):
            print(f"{i}. {ganador}")

except ValueError:
    print("Error: Ingresa un número válido.")

