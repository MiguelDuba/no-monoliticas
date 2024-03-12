import psycopg2

def get_cursor():
    conn = psycopg2.connect(database="companies_db",
                        host="localhost",
                        user="admin",
                        password="admin",
                        port="5434")
    conn.autocommit = True
    cursor = conn.cursor()
    return cursor


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