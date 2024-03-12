class Address:
    def __init__(self, address1, address2, address3, contry, zip_code, city) -> None:
        self.address1 = address1
        self.address2 = address2
        self.address3 = address3
        self.contry = contry
        self.zip_code = zip_code
        self.city = city

class Company:
    def __init__(self, id, name, age, description, address) -> None:
        self.id = id
        self.name = name
        self.age = age
        self.description = description
        self.address = address