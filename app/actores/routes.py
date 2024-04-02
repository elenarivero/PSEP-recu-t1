from flask import Blueprint
from utils.functions import *

rutaActores = "ficheros/actores.json"
actoresBP = Blueprint('actores', __name__)

@actoresBP.delete('/<int:id>')
def borraActor(id):
    listaActores = leeFichero(rutaActores)
    for actor in listaActores:
        if actor["id"] == id:
            listaActores.remove(actor)
            escribeFichero(listaActores, rutaActores)
            return {}, 200
    return {"error": "actor no encontrado"}, 404