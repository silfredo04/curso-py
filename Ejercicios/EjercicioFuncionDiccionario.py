def listarTermino(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} : {value}")


diccionario = {
    'nombre':'silfredo',
    'apellido': 'orozco',
    'edad':31
}

print(listarTermino(nombre = 'silfredo'))


def desplegarNombre(nombres):
    for nombre in nombres:
        print(nombre)

nombres = ['juan','milena','daniel']

desplegarNombre(nombres)