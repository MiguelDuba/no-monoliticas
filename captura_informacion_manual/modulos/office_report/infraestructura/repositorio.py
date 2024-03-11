from config.db import get_cursor

def create_office_report(data):
    cursor = get_cursor()
    query = """ insert into officereport(id, direccion, oficinas, banos,descripcion, created_date) VALUES (%s, %s, %s, %s, %s, CURRENT_TIMESTAMP) """
    cursor.execute(query, (data.id, data.direccion, data.oficinas, data.banos, data.descripcion))
