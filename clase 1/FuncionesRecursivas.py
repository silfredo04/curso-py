# calular el factorial de un numero 

num = int(input("ingrese un numero: "))

def calcularFactorial(numero):
    if numero == 1:
        return numero
    else:
        return numero * calcularFactorial(numero-1)
    

resultado = calcularFactorial(num)
print(f'el factorial de {num} es {resultado}')