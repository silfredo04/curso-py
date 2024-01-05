import tkinter as tk
from Persona import Persona

def agregar_persona():
    nombre = nombre_entry.get()
    apellido = apellido_entry.get()
    edad = edad_entry.get()

    persona = Persona(nombre, apellido, edad)
    persona.agregar_persona()

    nombre_entry.delete(0, tk.END)
    apellido_entry.delete(0, tk.END)
    edad_entry.delete(0, tk.END)

root = tk.Tk()
root.title("Agregar Persona")

nombre_label = tk.Label(root, text="Nombre:")
nombre_label.grid(row=0, column=0, padx=5, pady=5)

nombre_entry = tk.Entry(root)
nombre_entry.grid(row=0, column=1, padx=5, pady=5)


apellido_label = tk.Label(root, text="Apellido:")
apellido_label.grid(row=1, column=0, padx=5, pady=5)

apellido_entry = tk.Entry(root)
apellido_entry.grid(row=1, column=1, padx=5, pady=5)

edad_label = tk.Label(root, text="Edad:")
edad_label.grid(row=2, column=0, padx=5, pady=5)

edad_entry = tk.Entry(root)
edad_entry.grid(row=2, column=1, padx=5, pady=5)

agregar_button = tk.Button(root, text="Agregar", command=agregar_persona)
agregar_button.grid(row=3, column=1, columnspan=2, padx=5, pady=5)

root.mainloop()

