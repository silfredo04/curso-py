class Rectangulo:
    """
        esta clase nos ayuda a calcular el area de un rectangulo
    """
    def __init__(self,b,h) -> None:
        self.b = b
        self.h = h

    def calcularArea(self):
        a = self.b * self.h
        return a


base = float(input("Proporciona la base: "))
altura = float(input("Proporciona la altura: "))

rectangulo = Rectangulo(base,altura)

area = rectangulo.calcularArea()

print(f'Area rectangulo: {area:.0f}')
