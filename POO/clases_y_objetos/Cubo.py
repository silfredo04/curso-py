class Cubo:
    """
    esta clase nos ayuda a calcular el volumen de un cubo
    """
    def __init__(self,ancho,profundo,alto) -> None:
        self.ancho = ancho
        self.profundo = profundo
        self.alto = alto

    def calcularVolumen(self):
        volumen = self.ancho * self.profundo * self.alto
        return volumen
    
ancho = float(input("Proporciona el ancho: "))
profundo = float(input("Proporciona la profundidad: "))
alto = float(input("Proporciona el alto: "))

cubo = Cubo(ancho,profundo,alto)

volumen = cubo.calcularVolumen()

print(f'El volumen es: {volumen:.0f} m^3')