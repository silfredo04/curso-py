class Producto:
    contador_id = 0

    @classmethod
    def incremento_id(cls):
        cls.contador_id +=1
        return cls.contador_id
    
    def __init__(self,nombre,precio) -> None:
        self.__idProducto = Producto.incremento_id()
        self.__nombre = nombre
        self.__precio = precio

    #get
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self,nombre):
        self.__nombre = nombre

    #get
    @property
    def precios(self):
        return self.__precio
    
    @precios.setter
    def precio(self,precio):
        self.__precio = precio

    def __str__(self) -> str:
        return f'Producto [id: {self.__idProducto} nombre: {self.__nombre} precio: {self.__precio}]'
    

if __name__ == '__main__':
    producto1 = Producto('camisa',30000)
    producto2 = Producto('pantalon',40000)
    print(producto1)
    print(producto2)
