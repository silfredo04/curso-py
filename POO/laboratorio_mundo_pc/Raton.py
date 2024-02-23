from DispositivoEntrada import DispositivoEntrada 
class Raton(DispositivoEntrada):
    idraton = 0

    @staticmethod
    def contador_ratones():
        Raton.idraton +=1
        return Raton.idraton
    
    def __init__(self, tipo_entrada, marca) -> None:
        super().__init__(tipo_entrada, marca)
        self._id = Raton.contador_ratones()

    def __str__(self) -> str:
        return f'[Raton: Id:{self._id} ]{super().__str__()} ||'
    
if __name__ == '__main__':
    raton1 = Raton('usb','hp')
    raton2 = Raton('blu','accer')
    print(raton1,raton2)