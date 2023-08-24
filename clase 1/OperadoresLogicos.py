"""
OPERADOR           DESCRIPCION                                           USO
and                Devuelve true si ambos operadores son true           a and b

or                 Devuelve true si alguno de los operadores es true    a or b

not                Devuelve true si alguno de los operadores es false    not a
"""
# Ejemplo

a = True
b = True

respuesta = a and b

print("operando con -> and: ",respuesta)

a = True
b = False

respuesta = a or b

print("operando con -> or: ",respuesta)


a = True
b = False

respuesta = not b

print("operando con -> not: ",respuesta)


#ejercicio de rango

valor = int(input("Por favor ingresa un valor: "))

rangoM = 5
minimo = 0
if(valor >= minimo and valor <= rangoM):
    print("Esta dentro del rango")
else:
    print("No esta dentro del rango")