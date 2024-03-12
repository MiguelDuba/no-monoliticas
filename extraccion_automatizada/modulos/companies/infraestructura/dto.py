from datetime import datetime

class AddCompanyMessage():
  def __init__(self, name, age, description, address):
    self.name = name
    self.age = age
    self.description = description
    self.address = address
    # self.updatedAt = datetime.now()

class AddAddres():
  def __init__(self, address1, address2, address3, contry, zip_code, city) -> None:
    self.address1 = address1
    self.address2 = address2
    self.address3 = address3
    self.contry = contry
    self.zip_code = zip_code
    self.city = city