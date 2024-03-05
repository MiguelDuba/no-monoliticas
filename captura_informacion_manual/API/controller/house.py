from flask import Flask
from flask import jsonify, request, Blueprint
from request.house_request import CreateHouse

# Crea una instancia de la aplicación Flask
app = Flask(__name__)


#user_schema = UserSchema()
users_api = Blueprint('users', __name__)

# Define una ruta para la página de inicio
@app.route('/')
def hello_world():
    return 'Hello, World!'

@users_api.route('/api/house/create', methods = ['POST'])
def create_user():
    json = request.get_json()
    fields_request = ["name", "age", "description", "address"]

    for field in fields_request:
        if field not in json:
            json[field]=""
    
    result = CreateHouse(json['id'],json['direccion'],json['habitaciones'],json['banos'],json['descripcion']).execute()    
    return jsonify(result), 201


# Ejecuta la aplicación si este archivo es el punto de entrada
if __name__ == '__main__':
    app.run(debug=True)