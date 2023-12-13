edad = int(input("Ingresa tu edad: "))


""" veinte = edad >= 20 and edad < 30
print(veinte)

treinta = edad >= 30 and edad < 40
print(treinta) """

if (edad >= 20 and edad < 30) or (edad >= 30 and edad < 40):
    #print('dentro de rango (20\'s) o (30\'s)')
    if (edad >= 20 and edad < 30):
        print('dentro de rango (20\'s)')
    elif (edad >= 30 and edad < 40):
        print('dentro de rango (30\'s)')
else:
    print("No esta dentro de los rango (20's) o (30's)")


if (20 <= edad < 30) or (30 <= edad < 40):
    #print('dentro de rango (20\'s) o (30\'s)')
    if (edad >= 20 and edad < 30):
        print('dentro de rango (20\'s)')
    elif (edad >= 30 and edad < 40):
        print('dentro de rango (30\'s)')
else:
    print("No esta dentro de los rango (20's) o (30's)")