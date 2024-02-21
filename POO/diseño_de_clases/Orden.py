from Producto import Producto

class Orden:
    contador_id = 0

    @classmethod
    def incremento_id(cls):
        cls.contador_id +=1
        return cls.contador_id
    

    def __init__(self,productos) -> None:
        self.__idOrden = Orden.incremento_id()
        self.__productos = list(productos)

    @property
    def productos(self):
        return self.__productos
    
    @productos.setter
    def productos(self,productos):
        self.__productos = productos


    def agregar_producto(self,producto):
        self.__productos.append(producto)



    def calcular_total(self):
        total = 0

        for producto in self.__productos:
            total += producto.precio

        return total


    def __str__(self) -> str:
        productos_str = ''

        for producto in self.__productos:
            productos_str += producto.__str__() + ' | '

        return f'[Orden id: {self.__idOrden} \nProductos: {productos_str}]'
    


if __name__ == '__main__':
    producto1 = Producto('camisa',30000)
    producto2 = Producto('pantalon',40000)
    productos1 = [producto1,producto2]
    orden1 = Orden(productos1)
    orden2 = Orden(productos1)
    print(orden1)
    print(orden2)
