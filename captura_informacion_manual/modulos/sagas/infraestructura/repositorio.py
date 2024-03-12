from config.db import get_cursor

def initialize_saga_log(data):
    cursor = get_cursor()
    query = """ insert into sagalog(id, transaction_id, step, status, details, resultado, create_time, end_time) VALUES (%s, %s, %s, %s, %s, %s, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP) """
    cursor.execute(query, (data.id, data.transaction_id, data.step, data.status, data.details, data.resultado))

def update_saga_log(data):
    cursor = get_cursor()
    query = """UPDATE sagalog SET end_time = CURRENT_TIMESTAMP, step = %s , status = %s , resultado = %s , details = %s WHERE transaction_id = %s"""
    cursor.execute(query, (data.step, data.status , data.resultado , data.details , data.transaction_id))
    
