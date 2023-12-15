from FiguraGeometrica import FiguraGeometrica
from Color import Color


class Rectangulo(FiguraGeometrica,Color):
    def __init__(self, alto, ancho,color) -> None:
        FiguraGeometrica.__init__(self,alto,ancho)
        Color.__init__(self,color)
        self.__area = 0

    def calcularArea(self):
        self.__area = self.alto * self.ancho
        return self.__area
    
    def __str__(self) -> str:
        return f'Alto -> {self.alto}, Ancho -> {self.ancho}, {Color.__str__(self)}, Area -> {self.__area}'