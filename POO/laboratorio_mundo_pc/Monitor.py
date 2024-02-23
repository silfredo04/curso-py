class Monitor:
    idmonitor = 0

    @staticmethod
    def contador_monitores():
        Monitor.idmonitor +=1
        return Monitor.idmonitor
    
    def __init__(self,marca,tamanio) -> None:
        self._id = Monitor.contador_monitores()
        self._marca = marca
        self._tamanio = tamanio

    @property
    def marca(self):
        return self._marca
    
    @marca.setter
    def marca(self,marca):
        self._marca = marca


    @property
    def tamanio(self):
        return self._tamanio
    
    @tamanio.setter
    def tamanio(self,tamanio):
        self._tamanio = tamanio

    def __str__(self) -> str:
        return f'[Monitor: Id: {self._id} Marca: {self._marca} Tamaño: {self._tamanio}] ||'
    

if __name__ == '__main__':
    monitor1 = Monitor('accer','15 pulgadas')
    print(monitor1)
