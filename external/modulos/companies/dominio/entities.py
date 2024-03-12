class CompanyReport:
    def __init__(self, id, companies_list,server_name, status, create_date) -> None:
        self.id = id
        self.companies_list = companies_list
        self.server_name = server_name
        self.status = status
        self.created_date = create_date

class CompanyData:
    def __init__(self, report_id, name, age, description, address, created_date) -> None:
        self.report_id = report_id
        self.name = name
        self.age = age
        self.description = description
        self.address = address
        self.created_date = created_date
class Config:
    def __init__(self, host, user, password) -> None:
        self.host = host
        self.user = user
        self.password = password

class Server:
    def __init__(self, id, name, type, config, created_date) -> None:
        self.id = id
        self.name = name
        self.type = type
        self.config = config
        self.created_date = created_date

