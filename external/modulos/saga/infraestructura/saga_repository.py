from config.postgres import get_cursor


def insert_saga_log(log):
    cursor = get_cursor()
    query = """ insert into saga_log(id, step, server ,status, created_date) VALUES (%s, %s, %s, %s, %s) """
    cursor.execute(query, (log.id, log.step, log.server, log.status, log.created_date))


def update_saga_log(log):
    cursor = get_cursor()
    query = """ update saga_log set status = %s,finished_date = CURRENT_TIMESTAMP where id = %s AND step = %s AND server = %s"""
    cursor.execute(query, (log.status, log.id, log.step, log.server))