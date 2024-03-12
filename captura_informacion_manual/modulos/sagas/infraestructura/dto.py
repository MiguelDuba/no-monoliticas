class SagaLogMessage:
    def __init__(self, id, transaction_id, step, status, details, create_time, end_time, resultado):
        self.id = id, 
        self.transaction_id = transaction_id, 
        self.step = step, 
        self.status =  status, 
        self.details  = details, 
        self.resultado = resultado,
        self.create_time = create_time, 
        self.end_time = end_time

        