import json
from urllib.request import urlopen
from Pelicula import Pelicula
class RespositorioPelicula(object):
    __conn=None
    __manejador=None
    __lista=[]
    def __init__(self,manejador):
        self.__conn = None
        self.__manejador=manejador
        self.__lista=[]
    
    def obtenerPeliculasApi(self):
        
        dJson=None
        url= 'https://api.themoviedb.org/3/discover/movie?api_key=6e23417f14bca07bb07e305123a7a55c'
        try:
            respuesta=urlopen(url)
        except:
            raise Exception('Fallo la conexión a la API, no se obtuvieron datos.')
        else:
            dJson=json.loads(respuesta.read())
            self.__lista=dJson['results']
            generosP=[{"id":28,"name":"Action"},{"id":12,"name":"Adventure"},{"id":16,"name":"Animation"},{"id":35,"name":"Comedy"},{"id":80,"name":"Crime"},{"id":99,"name":"Documentary"},{"id":18,"name":"Drama"},{"id":10751,"name":"Family"},{"id":14,"name":"Fantasy"},{"id":36,"name":"History"},{"id":27,"name":"Horror"},{"id":10402,"name":"Music"},{"id":9648,"name":"Mystery"},{"id":10749,"name":"Romance"},{"id":878,"name":"Science Fiction"},{"id":10770,"name":"TV Movie"},{"id":53,"name":"Thriller"},{"id":10752,"name":"War"},{"id":37,"name":"Western"}]
            for pelicula in self.__lista:
                banderaDos=True
                generos=''
                for idGenero in pelicula['genre_ids']:
                    bandera=True
                    i=0
                    while i < len(generosP) and bandera:
                        if generosP[i]['id']==idGenero:
                            bandera = False
                        else:
                            i+=1
                    if banderaDos:
                        generos+='{}'.format((generosP[i]['name']))
                        banderaDos=False
                    else:
                        generos+=',{}'.format((generosP[i]['name']))
                peliculaNueva=Pelicula(pelicula['original_title'],pelicula["overview"],pelicula['original_language'],pelicula["release_date"],generos)
                self.agregarPelicula(peliculaNueva)
            
            
    def obtenerListaPeliculas(self):
        return self.__manejador.getListaPelicula()
    def agregarPelicula(self, pelicula):
        self.__manejador.agregarPelicula(pelicula)
        return pelicula