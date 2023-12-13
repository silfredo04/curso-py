"""
    Proporciona tu edad:

    0-10 La infancia es increible...
    10-20 Muchos cambios y muchos estudios...
    20-30 Amor y comienza el trabajo...

    cualquier oto valor: etapa de vida no reconocida
"""
edad = int(input("Por favor proporciona tu edad: "))


if 0 <= edad < 10:
    print(f"La infancia es increible...")
elif 10 <= edad < 20:
    print("Muchos cambios y muchos estudios...")
elif 20 <= edad < 30:
    print("Muchos cambios y muchos estudios...")
else:
    print("etapa de vida no reconocida...")