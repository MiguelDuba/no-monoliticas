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

class SagaLog:
    def __init__(self, id, step, server,status, created_date, finished_date) -> None:
        self.id = id
        self.step = step
        self.server = server
        self.status = status
        self.finished_date = finished_date
        self.created_date = created_date