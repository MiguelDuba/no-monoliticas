from flask import Flask
from flask import jsonify, request, Blueprint
from ..requests.house_request import CreateHouse
from core.service.house_service import create_house_service

house_api = Blueprint('houses', __name__)

@house_api.route('/api/house/create', methods = ['POST'])
def create_user():
    json = request.get_json()
    fields_request = ["name", "age", "description", "address"]

    for field in fields_request:
        if field not in json:
            json[field]=""
    
    result = CreateHouse(json['id'],json['direccion'],json['habitaciones'],json['banos'],json['descripcion'])
    create_house_service(result)

    return "Casa Creada", 201
