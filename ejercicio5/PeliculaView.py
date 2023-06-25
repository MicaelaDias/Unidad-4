import tkinter as tk
from PeliculaList import PeliculaList
from UpdatePeliculaForm import UpdatePeliculaForm
class PeliculaView(tk.Tk):
    def __init__(self): 
        super().__init__() 
        self.title("Lista de Peliculas") 
        self.list = PeliculaList(self, height=15) 
        self.form=UpdatePeliculaForm(self)
         
        self.list.pack(side=tk.LEFT, padx=10, pady=10) 
        self.form.pack(padx=10, pady=10) 
        
    def agregarPelicula(self, pelicula):
        self.list.insertar(pelicula)
    
    def setControlador(self, ctrl): #vincula la vista con el controlador 
        
        self.list.bind_doble_click(ctrl.seleccionarPelicula)
    def obtenerDetalles(self): 
        return self.form.crearPeliculaDesdeFormulario()
    def verPeliculaEnForm(self, pelicula): 
        self.form.mostrarEstadoPeliculaEnFormulario(pelicula)