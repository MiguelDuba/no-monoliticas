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

class Cadastral:
    def __init__(self, age, address) -> None:
        self.age = age
        self.address = address

class CadastralHandler(tornado.web.RequestHandler):
    
    def set_default_headers(self):
        self.set_header("Content-Type", 'application/json')
    
    def get(self):
        faker = Faker()
        faker.add_provider(address)
        cadastal_size = random.randint(100,500)
        houses = []
        for _ in range(cadastal_size):
            address_fake = Address(
                faker.street_address(),
                faker.street_name(),
                faker.street_suffix(),
                faker.country_code(),
                faker.postcode(),
                faker.city()
            )
            house_fake = Cadastral(
                random.randint(5,50),
                address_fake.__dict__
            )
            houses.append(house_fake.__dict__)
        print(f"Send  Cadastral {len(houses)} from mock server")
        response = {
            "houses" : houses
        }
        self.finish(json.dumps(response))