class Miclase:

    # variable de clase 
    variable_clase = "mi variable de clases"

    def __init__(self,variable_objeto) -> None:
        self.variable_objeto = variable_objeto

    #metodo estatico 
    @staticmethod
    def metodo_estatico():
        print(Miclase.variable_clase)

    @classmethod
    def metodo_clase(cls):
        print(cls.variable_clase)

    def metodo_instancia(self):
        self.metodo_estatico()
        self.metodo_clase()
        print(self.variable_clase)
        print(self.variable_objeto)

# acceder a mi variable de clases
print(Miclase.variable_clase)


# variable al vuelo 

Miclase.variable2 = "variable al vuelo"

miclase = Miclase("Mi variable de objeto")

print(miclase.variable_objeto)
print(Miclase.variable2)

Miclase.metodo_estatico()

Miclase.metodo_clase()

miclase1 = Miclase('variable_objeto')
miclase1.metodo_clase()
miclase1.metodo_instancia()


