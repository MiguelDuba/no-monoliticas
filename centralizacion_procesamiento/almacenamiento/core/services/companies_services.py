import json, uuid
from out.adapter.db.postgres import guardar_informacion_compania, create_tables
from ..domain.compania import Address, Company


def guardar_info_companias(ch, method, properties, body):
    body = json.loads(body)
    print(f'Message {body}')
    try:
        adress = Address(body["address"]["address1"], body["address"]["address2"], body["address"]["address3"], body["address"]["contry"], body["address"]["zip_code"], body["address"]["city"])
        compania = Company(str(uuid.uuid4()), body["name"], body["age"], body["description"], adress.__dict__)
        guardar_informacion_compania(compania)
        print("Información de compañía almacenada")

    except Exception  as e:
        print(e)

def seed_companies_db():
    create_tables()