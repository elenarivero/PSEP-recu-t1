from flask import Blueprint, jsonify, request
from utils.functions import *

rutaActores = "ficheros/actores.json"
rutaPeliculas = "ficheros/peliculas.json"

actoresBP = Blueprint('actores', __name__)

@actoresBP.get('/')
def getActores():
    actores = leeFichero(rutaActores)
    return jsonify(actores), 200

@actoresBP.post('/')
def anyadeActor():
    actores = leeFichero(rutaActores)
    peliculas = leeFichero(rutaPeliculas)

    if request.is_json:
        nuevo_actor = request.get_json()
        for pelicula in peliculas:
            if pelicula["id"] == nuevo_actor["id_pelicula"]:
                nuevo_actor["id"] = nuevo_id(actores)
                actores.append(nuevo_actor)
                escribeFichero(actores, rutaActores)
                return nuevo_actor, 201
                #se añadiría el actor a la lista de actores
                # calcula el nuevo id

        return {"error": "La película no existe"}, 404
    return {"error": "JSON no correcto"}, 415