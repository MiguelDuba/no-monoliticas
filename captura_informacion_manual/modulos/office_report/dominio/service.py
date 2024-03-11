from datetime import datetime, timezone 
from ..infraestructura.despachador import event_office_report_create
from ..infraestructura.repositorio import create_office_report
from .entidades import OfficeReport

def create_office_report_service(officereportcreate):
    
    office = OfficeReport(officereportcreate.id, officereportcreate.direccion, officereportcreate.oficinas, officereportcreate.banos, officereportcreate.descripcion)
    
    create_office_report(office)
    event_office_report_create(office)
