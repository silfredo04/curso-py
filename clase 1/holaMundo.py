print('hola mundo')

print('saludos desde python')


# tipos de variables 

miNombre = "silfredo"

print(miNombre)

miNombre = 20

print(miNombre)

x = 20
y = 10

z = x + y
print("El resultado de la suma es {}: ".format(z))
# con la funcion id() podemos saber la direccion de memoria de una variable 
print(id(z))

nombre = "silfredo orozco"
telefono = 30175845475
corre = "sorozco25@.edu.co"

print("Los datos agregados son: nombre: {}, telefono: {}, correo: {}".format(nombre,telefono,corre))

# tipos de datos las variables son dinamicas en python 

# tipo bool
x = True

print(type(x))

# tipo bool
x = False

print(type(x))

# tipo int
x = 10

print(type(x))

# tipo float
x = 10.6

print(type(x))

# tipo str
x = 'Hola'

print(type(x))

# cadena (str)

miGrupo = 'Mana'
banda = 'mexicana'

print("Mi grupo favorito es: "+ miGrupo + " " + banda)

print("Mi grupo favorito es: ",miGrupo,banda)

numero1 = '1'
numero2 = '2'

print("Concatenar: ",numero1 + numero2)

print("sumar: ", int(numero1)+int(numero2))

numero1 = 1
numero2 = 2

print(numero1+numero2)

#tipo bool

bandera = False 
print(bandera)

bandera = 3 > 2

if bandera:
    print("es verdadero")
else:
    print("es falso")
