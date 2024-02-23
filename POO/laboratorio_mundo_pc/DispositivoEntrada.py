class DispositivoEntrada:

    identrada = 0

    @staticmethod
    def asignarid():
        DispositivoEntrada.identrada +=1
        return DispositivoEntrada.identrada

    def __init__(self,tipo_entrada,marca) -> None:
        self._id = DispositivoEntrada.asignarid()
        self._tipo_entrada = tipo_entrada
        self._marca = marca

    #get
    @property
    def tipo_entrada(self):
        return self._tipo_entrada
    
    #setter
    @tipo_entrada.setter
    def tipo_entrada(self,tipo_entrada):
        self._tipo_entrada = tipo_entrada

    
    #get
    @property
    def marca(self):
        return self._marca
    
    #setter
    @marca.setter
    def marca(self,marca):
        self._marca = marca

    #str
    def __str__(self) -> str:
        return f' [Dispositivo de entrada: Id:{self._id} Tipo de entrada: {self._tipo_entrada} Marca: {self._marca}] ||'
    

if __name__ == '__main__':
    dispoen1 = DispositivoEntrada('usb','hp')
    dispoen2 = DispositivoEntrada('blu','accer')
    print(dispoen1,dispoen2)



    