from Empleado import Empleado

class Gerente(Empleado):
    contar_id= 0

    @classmethod
    def contarides(cls):
        cls.contar_id +=1
        return cls.contar_id
    
    def __init__(self,nombre,sueldo,departamento) -> None:
        super().__init__(nombre,sueldo)
        self.__id = Gerente.contarides()
        self.__departamento = departamento

    @property
    def departamento(self):
        return self.__departamento
    
    @departamento.setter
    def departamento(self,departamento):
        self.__departamento = departamento

    def __str__(self) -> str:
        return f'[Gerente {self.__id} Departamento: {self.__departamento}] {super().__str__()}'

""" def oper(a,b):
    return a * b
    

condicion = 1
while condicion == 1:
    a = int(input("primer valor: "))
    b = int(input("segundo valor: "))
    print(oper(a,b))
    condicion = int(input("para continuar precione 1 de lo contrario 0: "))

print("Gracias....!") if condicion == 0 else '' """