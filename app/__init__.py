from flask import Flask
from actores.routes import actoresBP
from pelicula.routes import peliculasBP

app = Flask(__name__)

app.register_blueprint(actoresBP, url_prefix='/actores')
app.register_blueprint(peliculasBP, url_prefix='/peliculas')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5351)