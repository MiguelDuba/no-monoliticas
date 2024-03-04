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