from DispositivoEntrada import DispositivoEntrada 
class Teclado(DispositivoEntrada):
    idteclado = 0

    @staticmethod
    def contador_teclados():
        Teclado.idteclado +=1
        return Teclado.idteclado
    
    def __init__(self, tipo_entrada, marca) -> None:
        super().__init__(tipo_entrada, marca)
        self._id = Teclado.contador_teclados()

    def __str__(self) -> str:
        return f'[Teclado: Id:{self._id} ]{super().__str__()} ||'
    
if __name__ == '__main__':
    teclado1 = Teclado('usb','hp')
    teclado2 = Teclado('blu','accer')
    print(teclado1,teclado2)