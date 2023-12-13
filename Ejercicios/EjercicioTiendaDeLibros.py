print("Proporcione los siguientes datos del libro: ")
Id = int(input("Proporcione el Id: "))
nombre = input("Proporcione el nombre del libro: ")
precio = float(input("Proporcione el precio: "))
envio = input("Indique si el envio es gratuito (True / False): ")


if envio == 'True':
    envio = True
elif envio == 'False':
    envio = False
else:
    envio = 'Valor incorrecto debe escribir True / False'

print('Id: ',Id)
print('Nombre: ',nombre)
print('Precio: ',precio)
print('Envio: ',envio)

print(f"""
         Id: {Id}
         Nombre: {nombre}
         Precio: {precio}
         Envio: {envio}
""")