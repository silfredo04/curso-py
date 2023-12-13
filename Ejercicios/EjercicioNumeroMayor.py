""" 
Instrucciones de tareas:
Solicitar al usuario dos valores, y determinar cual numero es el mayor
solicitar al usuario dos valores:
numero1 (int)
numero2 (int)
se deve imprimir el mayor de los dos numeros (la salida debe ser identica a la que sigue):
Proporciona el numero1:
Proporciona el numero2:
El numero mayor es:<numeroMayor>
 """

# definir variable 
numero1 = int(input("Proporciona el numero1: "))
numero2 = int(input("Proporciona el numero2: "))

if numero1 > numero2:
    numeroMayor = numero1
else:
    numeroMayor = numero2

print(f"El numero mayor es:{numeroMayor}")