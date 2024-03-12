import uuid, json
from datetime import datetime, timezone
from .entities import CompanyReport, CompanyData, Config, Server
from ..infraestructura.server_repositorio import get_server
from ..infraestructura.rest_server import get_companies
from ..infraestructura.ftp_server import get_file_data, get_files_names
from ..infraestructura.report_repository import save_company_report
from ..infraestructura.despachadores import evento_company_report_created

def consultar_compania_servidor(conpany_report):
    print(f"Comando para consultar a {conpany_report.server_name} companies")
    server = get_server(conpany_report.server_name)
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
    conpany_report.companies_list = report["companies"]
    print(f"Record to create {conpany_report.id} with {len(conpany_report.companies_list)} with date {conpany_report.created_date}")
    save_company_report(conpany_report)
    for company in conpany_report.companies_list:
        company_report = CompanyData(conpany_report.id, 
                                       company["name"],
                                       company["age"],
                                       company["description"],
                                       company["address"],
                                       conpany_report.created_date.strftime("'%Y-%m-%dT%H:%M:%SZ"))
        #print(f"Company Record to send {company_report.report_id} for {company_report.name} with date {company_report.created_date}")
        evento_company_report_created(company_report.__dict__)
    print(f"Report {conpany_report.id} finish")




def ejecutar_rest_call(server):
    return get_companies(server.config)

def cargar_archivos_ftp(server):
    files = get_files_names(server.config)
    reports = []
    for file in files:
        report = get_file_data(server.config, file)
        reports += report['companies']
    return {
        "companies": reports
    }

def get_server_by_name(server_name):
    server = get_server(server_name)
    if server == None:
        print("Servidor no encontrado")
        raise Exception("Servidor no encontrado")
    return server