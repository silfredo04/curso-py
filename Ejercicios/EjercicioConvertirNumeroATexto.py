numero = int(input("Ingrese numero del 1 al 3:  "))

numeroTexto = ''

if numero == 1:
    numeroTexto = 'Uno'
elif numero == 2:
    numeroTexto = 'Dos'
elif numero == 3:
    numeroTexto = 'Tres'
else:
    numeroTexto = 'Numero invalido'


print(f"""
    Numero proporcionado: {numero} - {numeroTexto}
""")


# sintaxis if else simplificada 

print("Es uno en sintaxis simplificada") if numero == 1 else print("no es uno sintaxis simplificada")