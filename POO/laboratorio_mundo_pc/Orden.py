from Monitor import Monitor 
from Teclado import Teclado
from Raton import Raton
from Computadora import Computadora
class Orden:
    idOrden = 0

    @staticmethod
    def contador_orden():
        Orden.idOrden +=1
        return Orden.idOrden
    
    def __init__(self,computadoras) -> None:
        self._id = Orden.contador_orden()
        self._computadoras = list(computadoras)

    @property
    def computadoras(self):
        return self._computadoras
    
    @computadoras.setter
    def computadoras(self,computadoras):
        self._computadoras = computadoras

    def agregarComputadora(self,computadora):
        self._computadoras.append(computadora)

    def __str__(self) -> str:
        computadoras_str = ''

        for computadora in self._computadoras:
            computadoras_str += computadora.__str__() + ' | '

        return f'[Orden id: {self._id} \nComputadoras: {computadoras_str}]'
    

if __name__ == '__main__':
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
    print(orden1)
    print(orden2)



