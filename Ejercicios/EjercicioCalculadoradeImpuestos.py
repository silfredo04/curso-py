""" Ejercicio: Calculadora de impuesto
    Crear una funcion para calcular el total de un pago incluyendo un impuesto aplicado.
    Formula: pago_total = pago_sin_impuesto + pago_sin_impuesto * (impuesto/100)
"""


pago_total=0
porcentaje = 100


def calculadoraDeImpuestos(p_s_i,im):
    pago_total = p_s_i + p_s_i * (im/porcentaje)
    print(pago_total)


pago_sin_impuesto = float(input("Proporcione el pago sin impuesto: "))
impuesto = float(input("Proporcione el monto del impuesto: "))

calculadoraDeImpuestos(pago_sin_impuesto,impuesto)


