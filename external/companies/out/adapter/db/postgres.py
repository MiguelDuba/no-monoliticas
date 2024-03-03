import psycopg2
import json

def get_cursor():
    conn = psycopg2.connect(database="companies_db",
                        host="localhost",
                        user="admin",
                        password="admin",
                        port="5432")
    conn.autocommit = True
    cursor = conn.cursor()
    cursor.execute(
            """ create table if not exists companies_report(
            id text,
            companies_list jsonb,
            create_date TIMESTAMP) """
        )
    return cursor


def save_records(data):
    cursor = get_cursor()
    query = """ insert into companies_report 
    select * from json_populate_recordset(NULL::companies_report, %s) """
    cursor.execute(query, (json.dumps(data),))