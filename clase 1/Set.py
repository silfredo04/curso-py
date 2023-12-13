
#Set
planetas = {'martes','jupiter','venus'}

print(planetas)

#largo
print(len(planetas))

#Revisar si un elemento esta precente

print('martes' in planetas)

#Agregar un elemento al Set

planetas.add('tierra')
print(planetas)

#No se puede agregar un elemento duplicado al Set

planetas.add('tierra')
print(planetas)

#Eliminar elemento posiblemente arrojando un error 
planetas.remove('tierra')
print(planetas)

#Eliminar elemento posiblemente sin arrojando un error 
planetas.discard('martes')
print(planetas)

# Limpiar Set

planetas.clear()
print(planetas)

#Eliminar la variable Set

del planetas

print(planetas)


