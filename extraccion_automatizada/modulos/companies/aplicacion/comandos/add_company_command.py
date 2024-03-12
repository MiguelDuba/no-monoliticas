from flask import Flask, jsonify, request, Blueprint
from ..dto import AddCompany, AddAddres
from ...dominio.company_service import add_companies_service

companies_blueprint = Blueprint('companie', __name__)

@companies_blueprint.route('/api/company/add', methods = ['POST'])
def add_company():

    json = request.get_json()
    fields_request = ["name", "age", "description", "address"]

    for field in fields_request:
        if field not in json:
            json[field]=""
    
    addres = AddAddres (json['address']['address1'], json['address']['address2'], json['address']['address3'],  json['address']['contry'],  json['address']['zip_code'],  json['address']['city'])
    result = AddCompany(json['name'], json['age'], json['description'],  addres)
    add_companies_service(result)
    
    return "Compañía agregada", 201