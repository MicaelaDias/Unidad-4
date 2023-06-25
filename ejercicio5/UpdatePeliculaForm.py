import tkinter as tk
from tkinter import messagebox
from PeliculaForm import PeliculaForm

class UpdatePeliculaForm(PeliculaForm):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
    def mostrarEstadoPeliculaEnFormulario(self,pelicula):
        super().mostrarEstadoPeliculaEnFormulario(pelicula)
      