from Monitor import Monitor 
from Teclado import Teclado
from Raton import Raton
from Computadora import Computadora
from Orden import Orden


monitor1 = Monitor("hp","15 pulgadas")
teclado1 = Teclado("usb","hp")
raton1 = Raton("usb","accer")
computadora1 =Computadora("Accer",monitor1,teclado1,raton1)
computadora2 =Computadora("Hp",monitor1,teclado1,raton1)
computadora3 =Computadora("Lenovo",monitor1,teclado1,raton1)
computadora4 =Computadora("PRM",monitor1,teclado1,raton1)
computadoras1 = [computadora1,computadora2,computadora3]
computadoras2 = [computadora4]
orden1 = Orden(computadoras1)
orden2 = Orden(computadoras2)
orden2.agregarComputadora(computadora1)
print(orden1)
print(orden2)