# class CoordinadorReportes():

#     def inicializar_pasos(self):
#     self.pasos = [
#         Inicio(index=0),
#         Transaccion(index=1, comando=ConsultarOfficeReport, evento=ReservaCreada, error=CreacionReservaFallida, compensacion=None),
#         Transaccion(index=2, comando=ConsultarOfficeReport, evento=ReservaPagada, error=PagoFallido, compensacion=RevertirPago),
#         Fin(index=3)
#     ]