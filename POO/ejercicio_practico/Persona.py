class Persona:
    contador_personas = 0

    @classmethod
    def generar_siguiente_valor(cls):
        cls.contador_personas +=1
        return cls.contador_personas

    def __init__(self,nombre,edad) -> None:
        self.__id_persona = Persona.generar_siguiente_valor()
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
        return f'Persona [id: {self.__id_persona} nombre: {self.__nombre} edad: {self.__edad}]'