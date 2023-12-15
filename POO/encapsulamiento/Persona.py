class Persona:
    """
        
        En esta clase, implementamos el encapsulamiento utilizando el símbolo '_'. 
        Esto indica que la variable dentro de la clase está restringida, 
        aunque aún se pueden realizar modificaciones. Por otro lado, al utilizar '__', 
        la variable queda más estrictamente restringida, ya que no acepta modificaciones desde fuera de la clase. 
        En este caso, solo se permite acceder y modificar la variable dentro de la clase misma.
    """
    def __init__(self,nombre,apellido,edad):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__edad = edad

    #decorador esto ayuda a que la variable encapsulada solo sea accedida por medio del metodo
    #Get
    @property  
    def nombre(self):
        return self.__nombre
    #Set
    @nombre.setter
    def nombre(self,nombre):
        self.__nombre = nombre
    
    #Get
    @property  
    def apellido(self):
        return self.__apellido
    
    #Set
    @apellido.setter
    def apellido(self,apellido):
        self.__apellido = apellido

    #Get
    @property  
    def edad(self):
        return self.__edad
    
    #Set
    @edad.setter
    def edad(self,edad):
        self.__edad = edad

    #metodo mostrar
    def mostrarDetalle(self):
        print(f'Persona: Nombre: {self.__nombre}  Apellido: {self.__apellido}  Edad: {self.__edad}')

    def __del__(self):
        print(f'Persona: {self.__nombre} {self.__apellido} {self.edad}')
        

if __name__ == '__main__':
    # instanciando una clase 
    persona1 = Persona('silfredo','orozco',32)
    persona1.nombre = 'silfredo orozco'
    # acceder a los métodos 
    persona1.mostrarDetalle()

    # otra manera de acceder a los métodos 
    Persona.mostrarDetalle(persona1)

    print(persona1.nombre)

    print(__name__)