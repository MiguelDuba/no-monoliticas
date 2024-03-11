from ..modulos.office_report.dominio.service import create_office_report_service

class Despachador:
    def __init__(self, id, direccion, oficinas, banos, descripcion):
        self.id = id
        self.direccion = direccion
        self.oficinas = oficinas
        self.banos = banos
        self.descripcion = descripcion

def event_despachar_office_report(officereportcreate):
    office = OfficeReport(officereportcreate.id, officereportcreate.direccion, officereportcreate.oficinas, officereportcreate.banos, officereportcreate.descripcion)
    
    create_office_report(office)
    event_office_report_create(office)