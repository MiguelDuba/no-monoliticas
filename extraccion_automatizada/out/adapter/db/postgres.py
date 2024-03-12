import psycopg2
import json


def get_cursor():
    conn = psycopg2.connect(database="companies_db",
                        host="localhost",
                        user="admin",
                        password="admin",
                        port="5434")
    conn.autocommit = True
    cursor = conn.cursor()
    return cursor


def guardar_informacion_compania(data):
    cursor = get_cursor()
    query = """ insert into companies (id, name, age, description, address) VALUES (%s, %s, %s, %s, %s) """
    cursor.execute(query, (data.id, data.name, data.age, data.description, json.dumps(data.address)))

def create_tables():
    cursor = get_cursor()

    cursor.execute(
            """ create table if not exists companies(
            id text,
            name text,
            age integer,
            description text,
            address jsonb) """
        )