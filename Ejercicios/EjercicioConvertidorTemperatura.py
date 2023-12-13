"""
Ejercicio: convertidor de temperatura
Realizar dos funciones para convertir de grados celsius a fahrenheit y viceversa
"""

def convertirCelsiusFahrenheit(gc):
    gradoFahrenheit = (gc*9/5) + 32
    return gradoFahrenheit

def convertirFahrenheitCelsius(gf):
    gradoFahrenheit = (gf - 32) *5/9
    return gradoFahrenheit


gradosCelsius = float(input("Grado celsius: "))
fahrenheit = convertirCelsiusFahrenheit(gradosCelsius)


print(f'Grado celsius {gradosCelsius} °C  a fahrenheit {fahrenheit} °F')


gradosFahrenheit = float(input("Grado fahrenheit: "))
celsius = convertirFahrenheitCelsius(gradosFahrenheit)


print(f'Grado fahrenheit {gradosFahrenheit} °F  a celsius {celsius} °C')
