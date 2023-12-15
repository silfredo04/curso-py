class Persona:

    def __init__(self,nombre,apellido,edad, *args, **kwargs):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.args = args
        self.kwargs = kwargs

    def mostrarDetalle(self):
        print(f'Persona: Nombre: {self.nombre}  Apellido: {self.apellido}  Edad: {self.edad}')
        i = 1
        for arg in self.args:
            print(f'Familia {i}: {arg}')
            i+=1
        for key, value in self.kwargs.items():
            print(f'Datos adicionales --> {key}: {value}')

# instanciando una clase 
persona1 = Persona('silfredo','orozco',32,'yadiris','danilo','paula','camilo',telefono='3014402213',direccion='calle 38 N 18-64')
persona1.telefono = 3014402213
persona2 = Persona('danilo','orozco',7)

""" #modificar un atributo

persona1.nombre = 'silfredo antonio'
persona2.nombre = 'danilo jose' """

""" print(f'Nombre: {persona1.nombre} Apellido: {persona1.apellido} Edad: {persona1.edad}')
print(f'Nombre: {persona2.nombre} Apellido: {persona2.apellido} Edad: {persona2.edad}') """

# acceder a los métodos 
persona1.mostrarDetalle()
print(persona1.telefono)
persona2.mostrarDetalle()
# otra manera de acceder a los métodos 
Persona.mostrarDetalle(persona1)