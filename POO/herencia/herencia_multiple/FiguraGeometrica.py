# convirtiendo esta clase abstracta ABC = Abstract Base Class
# no se puede instanciar esta clase ya que es abstracta
from abc import ABC, abstractmethod


class FiguraGeometrica(ABC):

    def __init__(self,alto,ancho) -> None:
        if self.__validarValor(alto):
            self.__alto = alto
        else:
            self.__alto = 0
            print("valor errado: ",alto)
        if self.__validarValor(ancho):
            self.__ancho = ancho
        else:
            self.__ancho = 0
            print("valor errado: ",ancho)

    #get y set 
    
    @property
    def alto(self):
        return self.__alto
    
    @alto.setter
    def alto(self,alto):
        if self.__validarValor(alto):
            self.__alto = alto
        else:
            print("valor errado: ",alto)
        

    @property
    def ancho(self):
        return self.__ancho
    
    @ancho.setter
    def ancho(self,ancho):
        if self.__validarValor(ancho):
            self.__ancho = ancho
        else:
            print("valor errado: ",ancho)

    @abstractmethod
    def calcularArea(self):
        pass


    def __validarValor(self,valor):
        return True if 0 < valor < 10 else False

    def __str__(self) -> str:
        return f'Alto -> {self.__alto}, Ancho -> {self.__ancho},'