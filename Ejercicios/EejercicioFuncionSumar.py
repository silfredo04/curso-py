"""
Crear una funcion para sumar los 
valores recibidos de tipo numerico,  utilizando argumentos variables 
*args comoparametros de la funcion y regresar como resultado la suma de todas los valores
pasados como argumento.

"""


#definimos nuestra funcion para sumar valores 
def sumarTodo (*args):
    resultado:int = 0
    for valor in args:
        #resultado = resultado + valor
        resultado += valor
    return resultado


#llamamos a la funcion para sumar
print(sumarTodo(1,2,3,56))

#definimos nuestra funcion para multiplicar valores 
def multiplicarTodo (*args):
    resultado:int = 1
    for valor in args:
        #resultado = resultado + valor
        resultado *= valor
    return resultado


#llamamos a la funcion para multiplicar
print(multiplicarTodo(1,2,3,56))