from Persona import Persona


if __name__ == '__main__':
    print('Creacion de objetos'.center(50,'-'))
    persona1 = Persona('Camilo','Sanchez',18)

    persona1.mostrarDetalle();

    print('Eliminacion de objetos'.center(50,'-'))
    del persona1
    print(__name__)