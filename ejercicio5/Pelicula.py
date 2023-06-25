import json
from urllib.request import urlopen
from urllib.error import URLError,HTTPError
class Pelicula:
    __titulo = ''
    __resumen = ''
    __lenguaje = ''
    __fecha=None
    __generos = ''
    def __init__(self,titulo='',resumen='',lenguaje='',fecha=None,genero=''):
        self.__titulo=titulo
        self.__resumen=resumen
        self.__lenguaje=lenguaje
        self.__fecha=fecha
        self.__generos=genero
    def getTitulo(self):
        return self.__titulo
    def getResumen(self):
        return self.__resumen
    def getLenguaje(self):
        return self.__lenguaje
    def getFecha(self):
        return self.__fecha
    def getGenero(self):
        return self.__generos
    