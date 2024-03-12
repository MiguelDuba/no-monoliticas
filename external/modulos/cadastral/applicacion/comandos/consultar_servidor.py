import uuid
from datetime import datetime, timezone
from ...dominio.service import consultar_cadastral_servidor
from ...dominio.entities import CadastralReport

class ConsultarCatastralServidor():
    def __init__(self, id, name) -> None:
        self.id = id
        self.name = name


def consultar_servidor_catrastal(consultarServidor):
    if consultarServidor.id is None:
        consultarServidor.id = str(uuid.uuid4())
    cadastral_report = CadastralReport(consultarServidor.id, None, consultarServidor.name, "Iniciado", datetime.now(timezone.utc))
    consultar_cadastral_servidor(cadastral_report)