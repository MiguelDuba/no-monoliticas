from ..dominio.entities import Config, Server

def map_server_entity(row):
    return Server(
        row[0],
        row[1],
        row[2],
        Config(row[3]['host'],row[3]['user'],row[3]['password']),
        row[4]
    )