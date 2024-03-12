from ...infraestructura.repositorio import initialize_saga_log, update_saga_log
from ...infraestructura.dto import SagaLogMessage
from ....office_report.dominio.service import querie_office_report_service
import uuid


# class CoordinadorReportes():

# Pasos
# 1. ConsultaOffices
# 2. ConsultaIndustrial
# 3. GuardarResultado
# 4. Fin 

#     def inicializar_pasos(self):
#     self.pasos = [
#         Inicio(index=0),
#         Transaccion(index=1, comando=ConsultarOfficeReport, evento=ReservaCreada, error=CreacionReservaFallida, compensacion=None),
#         Transaccion(index=2, comando=ConsultarOfficeReport, evento=ReservaPagada, error=PagoFallido, compensacion=RevertirPago),
#         Fin(index=3)
#     ]

def saga_procesar_reporte():
    ##  ConsultarOfficeReport
    try:
        
        data_saga = SagaLogMessage(None, None, None, None, None, None, None, None)
        data_saga.id = str(uuid.uuid4())
        data_saga.transaction_id = str(uuid.uuid4())
        data_saga.step = "1"
        data_saga.status = "started"
        iniciar_saga(data_saga)
        
        totaloffice = querie_office_report_service()
        data_saga.status = "success"
        actualizar_saga(data_saga)
        
        ##  totalindustrial = ConsultaIndustrial
        ##  GuardarResultado

        total = totaloffice # + totalindustrial 
        data_saga.resultado = "Total registros encontrados" + str(total)
        data_saga.status = "ended"
        data_saga.step = "3"
        terminar_saga(data_saga)
        return total
    
    except Exception as e:
        data_saga.status = "error"
        data_saga.details = str(e)
        data_saga.transaction_id = data_saga.transaction_id
        actualizar_saga(data_saga)
        raise e

def iniciar_saga(data):
    #data = SagaLogMessage(data.id, data.transaction_id, data.step, data.status, data.details, data.create_time, data.end_time, data.resultado)
    initialize_saga_log(data)

def actualizar_saga(data):
    update_saga_log(data)

def terminar_saga(data):
    update_saga_log(data)