import json
from .mapper import map_server_entity
from config.postgres import get_cursor

def get_server(name):
    cursor = get_cursor()
    query = """ select id, name, type, config, created_date from server where name = %s """
    cursor.execute(query, (name,))
    if cursor.rowcount == 0:
        return None
    else:
        server = None
        row = cursor.fetchone()
        while row is not None:
            server = row
            row = cursor.fetchone()
        return map_server_entity(server)
    

def create_server(server):
    cursor = get_cursor()
    query = """ insert into server(id, name, type, config,created_date) VALUES (%s, %s, %s, %s, %s) """
    cursor.execute(query, (server.id, server.name, server.type, json.dumps(server.config), server.created_date))