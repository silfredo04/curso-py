def mi_funcion():
    print("imprimiendo dentro de mi funcion")

mi_funcion()


# pasar parametros o argumentos a una funcion


def sumar(a,b):
    return a + b

resultado = sumar(3,6)
# llamamos la fincion e imprimimos en consola
print(f'El resultado de la suma es: {resultado}') 


# parametrospor default

def resta(a = 0, b=0) -> int:
    return a-b


print(f'La resta es: {resta(5-2)}')

# Argumentos variables en una funcion

def listarNombres (*args):
    respuesta = [] 
    for nombre in args:
        respuesta.append(nombre)
    return respuesta


res = listarNombres('Silfredo','Yadiris','Danilo','Camilo','Paula')

for r in res:
    print(r)


def listarNombres2 (*nombres):
    for nombre in nombres:
        print(nombre)

listarNombres2('Edwin','Milena','Keyla','Daniel')
listarNombres2('Silfredo','Yadiris','Danilo','Camilo','Paula')