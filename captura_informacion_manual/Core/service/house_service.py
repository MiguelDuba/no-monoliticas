from datetime import datetime, timezone 
from out.adapter.db.postgres import create_house
from out.adapter.produccer.send_house_info import send_house_data
from out.adapter.db.postgres import create_tables
from core.dominio.house import House

def create_house_service(body):
    print(f'Request {body}')
    house = House(body.id, body.direccion, body.habitaciones, body.banos, body.descripcion)
    print ("Housee", house)
    create_house(house)
    print ("Casa Creada")
    send_house_data(house.__dict__)
    print ("Casa Enviada")

def seed_companies_db():
    create_tables()
