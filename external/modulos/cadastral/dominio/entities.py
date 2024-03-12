class CadastralReport:
    def __init__(self, id, houses_list,server_name, status, create_date) -> None:
        self.id = id
        self.houses_list = houses_list
        self.server_name = server_name
        self.status = status
        self.created_date = create_date

class CadastralData:
    def __init__(self, report_id, address, created_date) -> None:
        self.report_id = report_id
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

