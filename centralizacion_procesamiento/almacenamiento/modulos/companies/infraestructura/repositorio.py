from config.db import get_cursor
import json

def guardar_informacion_compania(data):
    cursor = get_cursor()
    query = """ insert into companies (id, name, age, description, address) VALUES (%s, %s, %s, %s, %s) """
    cursor.execute(query, (data.id, data.name, data.age, data.description, json.dumps(data.address)))
