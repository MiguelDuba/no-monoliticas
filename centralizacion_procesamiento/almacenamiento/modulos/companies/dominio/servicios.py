from .entidades import Company, Address
from ..infraestructura.repositorio import guardar_informacion_compania
import json, uuid


def add_companies_service(ch, method, properties, body):  
    print(f'Request {body}')
    body = json.loads(body)

    try:
        adress = Address(body["address"]["address1"], body["address"]["address2"], body["address"]["address3"], body["address"]["contry"], body["address"]["zip_code"], body["address"]["city"])
        compania = Company(str(uuid.uuid4()), body["name"], body["age"], body["description"], adress.__dict__)
        guardar_informacion_compania(compania)
        print("Información de compañía almacenada")

    except Exception  as e:
        print(e)
