from Orden import Orden
from Producto import Producto

producto1 = Producto('camisa',30000)
producto2 = Producto('pantalon',40000)
producto3 = Producto('zapatos',80000)
producto4 = Producto('perfume',40000)


productos1 = [producto1,producto2]
productos2 = [producto3,producto4]

# se agrega una lista de productos
orden1 = Orden(productos1)
# se agrega un producto a la ves adcediendo al metodo agregar_producto
orden1.agregar_producto(producto3)
orden1.agregar_producto(producto4)
print(orden1)
print('Total: ',orden1.calcular_total())

orden2 = Orden(productos2)
print(orden2)
print('Total: ',orden2.calcular_total())