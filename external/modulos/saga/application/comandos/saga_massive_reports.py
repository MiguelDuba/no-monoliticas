import uuid
from datetime import datetime, timezone
from ....companies.applicacion.comandos.consultar_servidor import consultar_servidor_compania, ConsultarCompaniaServidor
from ....cadastral.applicacion.comandos.consultar_servidor import consultar_servidor_catrastal, ConsultarCatastralServidor
from ...infraestructura.server_repositorio import get_servers
from ...dominio.entities import SagaLog
from ...infraestructura.saga_repository import insert_saga_log, update_saga_log
from ...infraestructura.despachador import evento_massive_report_fail


def saga_log_start(id, status, step, server):
    log = SagaLog(id, step, server , status, datetime.now(timezone.utc),None)
    insert_saga_log(log)

def update_log_start(id, status, step):
    log = SagaLog(id, step, None, status, None, None)
    update_saga_log(log)

def consulta_comando_company(server, id):
    saga_log_start(id, "START", "ConsultarCompanies", server.name)
    try:
        compania = ConsultarCompaniaServidor(id, server.name)
        consultar_servidor_compania(compania)
        update_log_start(id, "DONE", "ConsultarCompanies")
    except Exception:
        update_log_start(id, "ERROR", "ConsultarCompanies")
        evento_massive_report_fail(id, server.name, "ConsultarCompanies")
    
def consulta_comando_catastral(server, id):
    saga_log_start(id, "START", "ConsultarCastastral", server.name)
    try:
        compania = ConsultarCatastralServidor(id, server.name)
        consultar_servidor_catrastal(compania)
        update_log_start(id, "DONE", "ConsultarCastastral")
    except Exception:
        update_log_start(id, "ERROR", "ConsultarCastastral")
        evento_massive_report_fail(id, server.name, "ConsultarCastastral")

def iniciar():
    id = str(uuid.uuid4())
    print(f"Saga massive report id {id}")
    servers = get_servers()
    for server in servers:
        consulta_comando_company(server, id)
        consulta_comando_catastral(server, id)
    print("Saga massive report id finish")
        

    
            
        



    