from Monitor import Monitor 
from Teclado import Teclado
from Raton import Raton

class Computadora:
    idcontador = 0

    @staticmethod
    def contador_computadoras():
        Computadora.idcontador +=1
        return Computadora.idcontador
    
    def __init__(self,nombre,monitor,teclado,raton) -> None:
        self._id = Computadora.contador_computadoras()
        self._nombre = nombre
        self._monitor = monitor
        self._teclado = teclado
        self._raton = raton

    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self,nombre):
        self._nombre = nombre
    
    @property
    def monitor(self):
        return self._monitor
    
    @monitor.setter
    def monitor(self,monitor):
        self._monitor = monitor
    
    @property
    def teclado(self):
        return self._teclado
    
    @teclado.setter
    def teclado(self,teclado):
        self._teclado = teclado


    @property
    def raton(self):
        return self._raton
    
    @raton.setter
    def raton(self,raton):
        self._raton = raton


    def __str__(self) -> str:
        return f'''
            {self._nombre}: {self._id}
            Monitor: {self._monitor}
            Teclado: {self._teclado}
            Raton: {self._raton}
        '''
    
if __name__ == '__main__':
    monitor1 = Monitor("hp","15 pulgadas")
    teclado1 = Teclado("usb","hp")
    raton1 = Raton("usb","accer")
    computadora1 =Computadora("Accer",monitor1,teclado1,raton1)
    print(computadora1)