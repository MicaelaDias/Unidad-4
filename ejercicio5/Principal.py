from ControladorPelicula import ControladorPeliculas
from PeliculaView import PeliculaView
from RepositorioPelicula import RespositorioPelicula
from ManejadorPelicula import ManejadorPeliculas
if __name__ == "__main__":
    
    manejador=ManejadorPeliculas()
    repo=RespositorioPelicula(manejador)
    repo.obtenerPeliculasApi()
    vista=PeliculaView()
    ctrl=ControladorPeliculas(repo, vista)
    vista.setControlador(ctrl)
    ctrl.start()
    