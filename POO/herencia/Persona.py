class Persona:

    def __init__(self,nombre,edad) -> None:
        self.__nombre = nombre
        self.__edad = edad
    
    #get
    @property
    def nombre(self):
        return self.__nombre
    
    #set
    @nombre.setter
    def nombre(self,nombre):
        self.__nombre = nombre

    #get
    @property
    def edad(self):
        return self.__edad
    
    #set
    @edad.setter
    def edad(self,edad):
        self.__edad = edad

    def __str__(self) -> str:
        return f'Persona --> Nombre: {self.__nombre}, Edad: {self.__edad}'



class Empleado(Persona):

    def __init__(self, nombre, edad,sueldo) -> None:
        super().__init__(nombre, edad)
        self.__sueldo = sueldo

    #get
    @property
    def sueldo(self):
        return self.__sueldo
    
    @sueldo.setter
    def sueldo(self,sueldo):
        self.__sueldo = sueldo

    def __str__(self) -> str:
        return f'Empleado --> Sueldo: {self.__sueldo}, {super().__str__()}'


if __name__ == '__main__':
    empleado = Empleado('Silfredo',32,1600000)

    print(empleado.nombre)
    print(empleado.edad)
    print(empleado.sueldo)