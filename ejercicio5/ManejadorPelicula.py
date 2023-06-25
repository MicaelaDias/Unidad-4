class ManejadorPeliculas:
    indice=0
    __listaPelicula = []
    def __init__(self):
        self.__listaPelicula=[]
    
    def agregarPelicula(self, pelicula): 
        pelicula.rowid=ManejadorPeliculas.indice
        ManejadorPeliculas.indice+=1
        
        self.__listaPelicula.append(pelicula)
    def getListaPelicula(self):
        return self.__listaPelicula
  
    def obtenerIndicePelicula(self,pelicula):
        bandera = False
        i=0
        while not bandera and i < len(self.__listaPelicula):
            if self.__listaPelicula[i].rowid == pelicula.rowid:
                bandera=True
            else:
                i+=1
        return i
    def updatePelicula(self,pelicula):
        indice=self.obtenerIndicePelicula(pelicula)
        self.__listaPelicula[indice]=pelicula
