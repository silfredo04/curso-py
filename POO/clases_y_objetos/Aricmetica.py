class Aricmetica:
    """
        clase aritmetica para realizar operaciones de sumar, restar, etc
    """
    def __init__(self,operandoA,operandoB) -> None:
        self.operandoA = operandoA
        self.operandoB = operandoB

    def sumar(self):
        return self.operandoA + self.operandoB
    
    def restar(self):
        return self.operandoA - self.operandoB
    
    def multiplicar(self):
        return self.operandoA * self.operandoB
    
    def dividir(self):
        return self.operandoA / self.operandoB
    


if __name__ == '__main__':
    aricmetica = Aricmetica(2,2)

    suma = aricmetica.sumar()
    resta = aricmetica.restar()
    multi = aricmetica.multiplicar()
    divi = aricmetica.dividir()
    print(f'Suma: {suma} Resta: {resta} Multiplicacion: {multi} Dividir: {divi:.0f}')