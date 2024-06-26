from flask import Flask
from flask_jwt_extended import JWTManager
from actores.routes import actoresBP
from pelicula.routes import peliculasBP
from users.routes import usersBP
import string
import secrets

alphabet = string.ascii_letters + string.digits
password = ''.join(secrets.choice(alphabet) for i in range(8))

app = Flask(__name__)

app.register_blueprint(actoresBP, url_prefix='/actores')
app.register_blueprint(peliculasBP, url_prefix='/peliculas')
app.register_blueprint(usersBP, url_prefix='/users')

app.config['SECRET_KEY'] = password

jwt = JWTManager(app)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5351)