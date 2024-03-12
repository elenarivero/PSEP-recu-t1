from flask import Blueprint
from utils.functions import *

peliculasBP = Blueprint('peliculas', __name__)
rutaPeliculas = "ficheros/peliculas.json"


@peliculasBP.get('/<int:id_pelicula>')
def getPelicula(id_pelicula):
    peliculas = leeFichero(rutaPeliculas)
    for pelicula in peliculas:
        if pelicula["id"] == id_pelicula:
            return pelicula, 200
    return {"error" : "Película no encontrada"}, 404