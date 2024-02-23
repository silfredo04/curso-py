from Empleado import Empleado
from Gerente import Gerente
def imprimir_detalle (objeto):
    print(objeto)
    print(type(objeto))
    if isinstance(objeto,Gerente):
        print(objeto.departamento)

empleado = Empleado("silfredo",5000)
imprimir_detalle(empleado)

gerente = Gerente("danilo",8000,"sistemas")
imprimir_detalle(gerente)