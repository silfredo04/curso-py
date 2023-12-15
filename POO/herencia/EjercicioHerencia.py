class Vehiculo:

    def __init__(self,color,ruedas) -> None:
        self.__color = color
        self.__ruedas = ruedas


    # get y set

    @property
    def color(self):
        return self.__color
    
    @color.setter
    def color(self,color):
        self.__color = color

    @property
    def ruedas(self):
        return self.__ruedas
    
    @ruedas.setter
    def ruedas(self,ruedas):
        self.__ruedas = ruedas

    def __str__(self) -> str:
        return f'Vehiculo --> Color: {self.__color} Ruedas: {str(self.__ruedas)}'
    


class Coche(Vehiculo):
    def __init__(self, color, ruedas,velocidad) -> None:
        super().__init__(color, ruedas)
        self.__velocidad = velocidad

    @property
    def velocidad(self):
        return self.__velocidad
    
    @velocidad.setter
    def velocidad(self,velocidad):
        self.__velocidad = velocidad


    def __str__(self) -> str:
        return f'Coche--> Velocidad: {str(self.__velocidad)} KM/HR, {super().__str__()}'
    

class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas,tipo) -> None:
        super().__init__(color, ruedas)
        self.__tipo = tipo

    @property
    def tipo(self):
        return self.__tipo
    
    @tipo.setter
    def tipo(self,tipo):
        self.__tipo = tipo

    def __str__(self) -> str:
        return f'Bicicleta --> Tipo: {self.__tipo}, {super().__str__()}'