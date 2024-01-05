import mysql.connector

class Persona:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def agregar_persona(self):
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="pruebapython"
        )

        mycursor = mydb.cursor()

        sql = "INSERT INTO personas (nombre, apellido, edad) VALUES (%s, %s, %s)"
        val = (self.nombre, self.apellido, self.edad)
        mycursor.execute(sql, val)

        mydb.commit()

        print(mycursor.rowcount, "registro(s) insertado(s).")