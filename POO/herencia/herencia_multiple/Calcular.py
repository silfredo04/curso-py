
from Cuadrado import Cuadrado
from Rectangulo import Rectangulo


print("Creacion de objeto cuadrado".center(50,'*'))

lado = int(input("Proporciona un lado: "))
color = input("Proporciona un color: ")

cuadrado = Cuadrado(lado,color)
cuadrado.calcularArea()
print(cuadrado)

#MRO - METHOD RESOLUTION ORDER // NOS AYUDA A VER EL ORDEN jerárquico  de como se estan llamando las clases heredadas
print(Cuadrado.mro())

print("Creacion de objeto Rectangulo".center(50,'*'))
alto = int(input("Proporcione su altura: "))
ancho = int(input("Proporcione su ancho: "))
colorR = input("Proporciona un color: ")

rectangulo = Rectangulo(alto,ancho,colorR)
rectangulo.calcularArea()

print(rectangulo)
