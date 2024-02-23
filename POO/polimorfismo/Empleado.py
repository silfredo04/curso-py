class Empleado:
    cotar_id = 0

    @classmethod
    def contar(cls):
        cls.cotar_id +=1
        return cls.cotar_id

    def __init__(self,nombre,sueldo) -> None:
        self.__id = Empleado.contar()
        self.__nombre = nombre
        self.__sueldo = sueldo

    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self,nombre):
        self.__nombre = nombre

    @property
    def sueldo(self):
        return self.__sueldo
    
    @sueldo.setter
    def sueldo(self,sueldo):
        self.__sueldo = sueldo

    def __str__(self) -> str:
        return f'Empleado {self.__id} Nombre: {self.__nombre} Sueldo: {self.__sueldo} ||'
    
    def mostrar_detalle(self):
        return self.__str__()


   
if __name__ == '__main__':
    empleado1 =Empleado('eduardo',1000000)
    empleado2 =Empleado('carlos',1000000)
    print(empleado1,empleado2)
    print(495-176)