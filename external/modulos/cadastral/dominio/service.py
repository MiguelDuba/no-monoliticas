import uuid, json
from datetime import datetime, timezone
from .entities import Config, Server, CadastralData, CadastralReport
from ..infraestructura.server_repositorio import get_server
from ..infraestructura.rest_server import get_cadastral
from ..infraestructura.ftp_server import get_file_data, get_files_names
from ..infraestructura.report_repository import save_cadastral_report
from ..infraestructura.despachadores import evento_cadastral_report_created

def consultar_cadastral_servidor(cadastral_report):
    print(f"Comando para consultar a {cadastral_report.server_name} cadastral")
    server = get_server(cadastral_report.server_name)
    if server == None:
        print("Servidor no encontrado")
        return
    if server.type == "REST":
        report = ejecutar_rest_call(server)
    elif server.type == "FTP":
        report = cargar_archivos_ftp(server)
    else:
        print(f"Type {server.type} not implemented yet")
        return
    cadastral_report.houses_list = report["houses"]
    print(f"Record to create {cadastral_report.id} with {len(cadastral_report.houses_list)} with date {cadastral_report.created_date}")
    save_cadastral_report(cadastral_report)
    for cadastral_item in cadastral_report.houses_list:
        cadastral = CadastralData(cadastral_report.id, 
                                       cadastral_item["address"],
                                       cadastral_report.created_date.strftime("'%Y-%m-%dT%H:%M:%SZ"))
        evento_cadastral_report_created(cadastral.__dict__)
    print(f"Report {cadastral_report.id} finish")




def ejecutar_rest_call(server):
    return get_cadastral(server.config)

def cargar_archivos_ftp(server):
    files = get_files_names(server.config)
    reports = []
    for file in files:
        report = get_file_data(server.config, file)
        reports += report['houses']
    return {
        "houses": reports
    }

def get_server_by_name(server_name):
    server = get_server(server_name)
    if server == None:
        print("Servidor no encontrado")
        raise Exception("Servidor no encontrado")
    return server