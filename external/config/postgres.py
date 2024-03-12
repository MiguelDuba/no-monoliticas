import psycopg2

def get_cursor():
    conn = psycopg2.connect(database="companies_db",
                        host="localhost",
                        user="admin",
                        password="admin",
                        port="5432")
    conn.autocommit = True
    cursor = conn.cursor()
    return cursor


def create_tables():
    cursor = get_cursor()
    # company report table
    cursor.execute(
            """ create table if not exists company_report(
            id text,
            companies_list jsonb,
            server_name text,
            status text,
            created_date TIMESTAMP) """
        )
    # server table
    cursor.execute(
            """ create table if not exists server(
            id text,
            name text,
            type text,
            config jsonb,
            created_date TIMESTAMP) """
        )
    
    cursor.execute(
            """ create table if not exists cadastral_report(
            id text,
            houses_list jsonb,
            server_name text,
            status text,
            created_date TIMESTAMP) """
        )
    
    cursor.execute(
            """ create table if not exists saga_log(
            id text,
            step text,
            server text,
            status text,
            created_date TIMESTAMP,
            finished_date TIMESTAMP) """
        )

    cursor.execute(
            """ 
            insert into server(id, name, type, config, created_date)
                select '1', 'REST_MOCK_SERVER', 'REST', '{"host": "http://localhost:8888", "user": "", "password":""}', CURRENT_TIMESTAMP
            where not exists (
                select 1 from server where name = 'REST_MOCK_SERVER'
            ) """
        )
    cursor.execute(
            """ 
            insert into server(id, name, type, config, created_date)
                select '2', 'FTP_MOCK_SERVER', 'FTP', '{"host": "localhost", "user": "user", "password":"123"}', CURRENT_TIMESTAMP 
            where not exists (
                select 1 from server where name = 'FTP_MOCK_SERVER'
            ) """
        )
    