import psycopg2
import json


def get_cursor():
    conn = psycopg2.connect(database="houses_db",
                        host="localhost",
                        user="admin",
                        password="admin",
                        port="5435")
    conn.autocommit = True
    cursor = conn.cursor()
    return cursor


def save_company_report(data):
    cursor = get_cursor()
    query = """ insert into company_report(id, companies_list, created_date) VALUES (%s, %s, %s) """
    cursor.execute(query, (data.id, json.dumps(data.companies_list), data.created_date))

def create_tables():
    cursor = get_cursor()
    # company report table
    cursor.execute(
            """ create table if not exists houses(
            id text,
            direccion text,
            habitaciones text,
            banos text,
            descripcion text,
            created_date TIMESTAMP) """
        )
    
def create_house(data):
    cursor = get_cursor()
    query = """ insert into houses(id, direccion, habitaciones, banos,descripcion, created_date) VALUES (%s, %s, %s, %s, %s, CURRENT_TIMESTAMP) """
    cursor.execute(query, (data.id, data.direccion, data.habitaciones, data.banos, data.descripcion))
