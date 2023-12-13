"""Imprimir numeros de 5 a 1 de manera desendente usando funciones recursivas.
puede ser cualquier valor positivo, ejemplo, si pasa el valor de 5, deve imprimir:
5
4
3
2
1

en caso de pasar el valor 3
3
2
1

Si se pasan valores negativos no imprimir nada"""

numero = int(input("Ingresa un numero: "))

def decremento(num):
    if num >= 1:
        print(num)
        decremento(num - 1)
    elif num == 0:
        return
    elif num <= 0:
        print('valor incorrecto..')


decremento(numero)
