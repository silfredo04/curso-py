#  definir la lista 
nombres = ['danilo','paula','camilo','yadiris']

# imprimir la lista
print(nombres)

#acceder a los elementos de una lista
print(nombres[0])
print(nombres[1])

# acceder a los elementos de manera inversa
print(nombres[-1])
print(nombres[-2])
#imprimir un rango
print(nombres[0:2]) #sin incluir el indice 2
#ir del inicio de la lista al indice (sin incluirlo)
print(nombres[:3]) 
#desde el indice indicado hasta el final
print(nombres[1:])
#cambiar un valor especificando un indice
nombres[2] = 'camilo emely'
print(nombres)

for nombre in nombres:
    print(nombre)

# con el len se ve la cantidad de elementos que hay en una lista
print(len(nombres))

# insertar un elemento en un indice en especifico
nombres.insert(1,'silfredo')
print(nombres) 
# remover un elemento 
nombres.remove('yadiris')
print(nombres)
# remover el ultimo valor agregado
nombres.pop()
print(nombres)
# eliminar un indice
del nombres[0]
print(nombres)
# rliminar la lista
nombres.clear()
print(nombres)
# borrar la lista por completo
del nombres
print(nombres)