import uuid
from datetime import datetime, timezone
from ...dominio.service import consultar_compania_servidor
from ...dominio.entities import CompanyReport

class ConsultarCompaniaServidor():
    def __init__(self, id, name) -> None:
        self.id = id
        self.name = name


def consultar_servidor_compania(consultarServidor):
    if consultarServidor.id is None:
        consultarServidor.id = str(uuid.uuid4())
    conpany_report = CompanyReport(consultarServidor.id, None, consultarServidor.name, "Iniciado", datetime.now(timezone.utc))
    consultar_compania_servidor(conpany_report)