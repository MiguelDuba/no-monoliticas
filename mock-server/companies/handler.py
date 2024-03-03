import tornado
import random
import json 
import datetime
from faker import Faker
from faker.providers import address
from faker.providers import company

class Address:
    def __init__(self, address1, address2, address3, contry, zip_code, city) -> None:
        self.address1 = address1
        self.address2 = address2
        self.address3 = address3
        self.contry = contry
        self.zip_code = zip_code
        self.city = city

class Company:
    def __init__(self, name, age, description, address) -> None:
        self.name = name
        self.age = age
        self.description = description
        self.address = address

class CompanyHandler(tornado.web.RequestHandler):
    
    def set_default_headers(self):
        self.set_header("Content-Type", 'application/json')
    
    def get(self):
        faker = Faker()
        faker.add_provider(address)
        faker.add_provider(company)
        companies_size = random.randint(5,10)
        companies = []
        for _ in range(companies_size):
            address_fake = Address(
                faker.street_address(),
                faker.street_name(),
                faker.street_suffix(),
                faker.country_code(),
                faker.postcode(),
                faker.city()
            )
            company_fake = Company(
                faker.company(),
                random.randint(5,50),
                faker.bs(),
                address_fake.__dict__
            )
            companies.append(company_fake.__dict__)
        response = {
            "companies" : companies
        }
        self.finish(json.dumps(response))


