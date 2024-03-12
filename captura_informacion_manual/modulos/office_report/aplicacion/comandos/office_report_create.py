from flask import Flask
from flask import jsonify, request, Blueprint
from ..dto import CreateOfficeReport
from ...dominio.service import create_office_report_service

office_report_api = Blueprint('office-report', __name__)

@office_report_api.route('/api/office-report/create', methods = ['POST'])
def create_office_report():
    json = request.get_json()
    fields_request = ["id", "direccion", "oficinas", "banos", "descripcion"]

    for field in fields_request:
        if field not in json:
            json[field]=""
    
    result = CreateOfficeReport(json['id'],json['direccion'],json['oficinas'],json['banos'],json['descripcion'])
    create_office_report_service(result)

    return "Reporte de Oficina Creada", 201
