import psycopg2
import json

def get_cursor():
    conn = psycopg2.connect(database="infomanual_db",
                        host="localhost",
                        user="admin",
                        password="admin",
                        port="5435")
    conn.autocommit = True
    cursor = conn.cursor()
    return cursor


def create_tables():
    cursor = get_cursor()
    # company report table
    cursor.execute(
            """ create table if not exists officereport(
            id text,
            direccion text,
            oficinas text,
            banos text,
            descripcion text,
            created_date TIMESTAMP) """
        )