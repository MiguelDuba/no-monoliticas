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
    # office report table
    cursor.execute(
            """ create table if not exists officereport(
            id text,
            direccion text,
            oficinas text,
            banos text,
            descripcion text,
            created_date TIMESTAMP) """
        )
    
        # office report table
    cursor.execute(
            """ create table if not exists sagalog(
            id text,
            transaction_id text,
            step text,
            status text,
            details text,
            resultado text,
            create_time TIMESTAMP,
            end_time TIMESTAMP) """
        )
    

