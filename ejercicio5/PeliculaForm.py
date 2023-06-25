import tkinter as tk
from tkinter import messagebox
from Pelicula import Pelicula
class PeliculaForm(tk.LabelFrame): 
    __fields = ("Titulo", "Resumen", "Lenguaje", "Fecha de lanzamiento","Género")
    def __init__(self, master, **kwargs): 
        super().__init__(master, text="Pelicula", padx=10, pady=10, **kwargs) 
        self.frame = tk.Frame(self) 
        self.entries = list(map(self.crearCampo, enumerate(self.__fields))) 
        self.frame.pack()
    def crearCampo(self, field): 
        position, text = field 
        label = tk.Label(self.frame, text=text) 
        entry = tk.Entry(self.frame, width=25) 
        label.grid(row=position, column=0, pady=5)
        entry.grid(row=position, column=1, pady=5) 
        return entry 
    def mostrarEstadoPeliculaEnFormulario(self, pelicula):
        # a partir de una pelicula, obtiene el estado
        # y establece en los valores en el formulario de entrada

        values = (pelicula.getTitulo(),pelicula.getResumen(),pelicula.getLenguaje(),pelicula.getFecha(),pelicula.getGenero())
        for entry, value in zip(self.entries, values):
            entry.delete(0, tk.END)
            entry.insert(0, value)
    
    def limpiar(self): 
        for entry in self.entries: 
            entry.delete(0, tk.END)
    def getFrame(self):
        return self.frame