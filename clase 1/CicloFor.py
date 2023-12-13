cadena = 'hola@hotmail.com'

bandera = False

for letra in cadena:
    if letra == '@':
        bandera = True
        break #rompe con el ciclo 
else:
    print('fin ciclo for')


print('es un correo valido') if bandera else print('No es un correo valido')
    
