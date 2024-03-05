from out.adapter.produccer.send_companies_info import send_company_data
from core.domain.company import Company, Address


def add_companies_service(body):  
    print(f'Request {body}')
    addres = Address(body.address.address1, body.address.address2, body.address.address3, body.address.contry, body.address.zip_code, body.address.city)
    company = Company(body.name, body.age, body.description, addres.__dict__)
    print ("Compañía", company)
    send_company_data(company.__dict__)
    print ("Casa Enviada")