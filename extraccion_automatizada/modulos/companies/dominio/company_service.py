from .entidades import Company, Address
from ..infraestructura.despachador import send_company_data


def add_companies_service(body):  
    print(f'Request {body}')
    addres = Address(body.address.address1, body.address.address2, body.address.address3, body.address.contry, body.address.zip_code, body.address.city)
    company = Company(body.name, body.age, body.description, addres.__dict__)
    print ("Compañía", company)


    send_company_data(company)