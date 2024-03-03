class Report:
    def __init__(self, id, companies_list, create_date) -> None:
        self.id = id
        self.companies_list = companies_list
        self.created_date = create_date

class CompanyReport:
    def __init__(self, report_id, name, age, description, address, created_date) -> None:
        self.report_id = report_id
        self.name = name
        self.age = age
        self.description = description
        self.address = address
        self.created_date = created_date