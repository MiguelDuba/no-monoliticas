from flask import Flask
from flask import jsonify, request, Blueprint
from ..coordinadores.saga_report import saga_procesar_reporte

saga_report_api = Blueprint('saga-report',__name__)

@saga_report_api.route('/api/saga-report/querie', methods = ['GET'])
def get_querie_report():
    print("inicia proceso saga")
    result = saga_procesar_reporte()
    message = f"Registros manuales creados: {result}"
    return message, 201