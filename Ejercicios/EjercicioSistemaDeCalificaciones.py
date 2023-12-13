"""
    Instruccion de la tarea:
    El objetivo del ejercicio es crear un sistema de calificaciones, como sigue:
    El usuario proporcionara un valor entre 0 y 10.
    si esta entre 9 y 10: Imprimir una A
    si esta entre 8 y menor a 9: Imprimir una B
    si esta entre 7 y menor a 8: Imprimir una C
    si esta entre 6 y menor a 7: Imprimir una D
    si esta entre 0 y menor a 6: Imprimir una F
    cualquier otro valor debe imprimir: valor incorrecto
    por ejemplo:
    Proporciona un valor entero 0 y 10:
    A
"""

print("sistema de calificaciones")

nota = int(input("Ingresa un valor entre 0 y 10: "))
resultado = None
if 9<= nota <= 10:
    resultado = 'A'
elif 8 <= nota < 9:
    resultado = 'B'
elif 7 <= nota < 8:
    resultado = 'C'
elif 6 <= nota < 7:
    resultado = 'D'
elif 0 <= nota < 6:
    resultado = 'F'
else:
    resultado = 'valor incorrecto'
print(resultado)