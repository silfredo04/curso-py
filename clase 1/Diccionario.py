#Diccionario (Key, value)


diccionario = {
    'nombre':'silfredo',
    'apellido': 'orozco',
    'edad':31
}
print(diccionario)

#Largo
print(len(diccionario))

#Acceder a un elemento por la key
print(diccionario['nombre'])

#Otra forma de recuperar un elemento 

print(diccionario.get('apellido'))

#Modificamos valor de un elemento 
diccionario['nombre'] = 'danilo'
print(diccionario)

# recorrer los elementos

for key, value in diccionario.items():
    print(key,':',value)

# recuperar solo las key
for key in diccionario.keys():
    print(key)

# recuperar solo las value
for value in diccionario.values():
    print(value)
#comprobar la existencia de algun elemento 

print('nombre' in diccionario)

#agregar un elemento al diccionario 

diccionario['pk'] = 'primary key'
print(diccionario)

#remover un elemento del diccionario
diccionario.pop('edad')
print(diccionario)

#limpiar el dicccionario sin eliminar la variable
diccionario.clear()
print(diccionario)

#eliminar el diccionario por completo

del diccionario

print(diccionario)