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
    

def get_servers():
    cursor = get_cursor()
    query = """ select id, name, type, config, created_date from server """
    cursor.execute(query, ())
    if cursor.rowcount == 0:
        return None
    else:
        servers = []
        row = cursor.fetchone()
        while row is not None:
            servers.append(map_server_entity(row))
            row = cursor.fetchone()
        return servers