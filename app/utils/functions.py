import json

def leeFichero(rutaFichero):
    archivo=open(rutaFichero, "r")
    data = json.load(archivo)
    archivo.close()
    return data

def escribeFichero(lista, rutaFichero):
    archivo = open(rutaFichero, "w")
    json.dump(lista, rutaFichero)
    archivo.close()
