import uuid, json
from datetime import datetime, timezone 
from core.domain.report import CompanyReport, Report
from core.domain.server import Server, Config
from out.adapter.rest.companies_call import get_companies_info
from out.adapter.db.postgres import save_company_report, create_tables, create_server, get_server
from out.adapter.ftp.client_ftp import get_file_data, get_files_names
from out.adapter.produccer.send_company_info import send_company_report

def start_companies_check(ch, method, properties, body):
    body = json.loads(body)
    print(f'Message {body}')
    server = get_server(body['name'])
    if server == None:
        print("Server not found")
        return
    if server.type == "REST":
        companies_report = get_rest(server)
    elif server.type == "FTP":
        companies_report = get_ftp(server)
    else:
        print("Type not implemented yet")
        pass
    report = Report(str(uuid.uuid4()), companies_report["companies"], datetime.now(timezone.utc))
    print(f"Record to create {report.id} with {len(report.companies_list)} with date {report.created_date}")
    save_company_report(report)
    for company in report.companies_list:
        company_report = CompanyReport(report.id, 
                                       company["name"],
                                       company["age"],
                                       company["description"],
                                       company["address"],
                                       report.created_date.strftime("'%Y-%m-%dT%H:%M:%SZ"))
        #print(f"Company Record to send {company_report.report_id} for {company_report.name} with date {company_report.created_date}")
        send_company_report(company_report.__dict__)
    print(f"Report {report.id} finish")


def seed_companies_db():
    create_tables()
    rest_mock = get_server("REST_MOCK_SERVER")
    if rest_mock is None:
        rest_mock = Server(
            str(uuid.uuid4()), 
            "REST_MOCK_SERVER", 
            "REST",
            Config("http://localhost:8888/companies", "", "").__dict__,
            datetime.now(timezone.utc))
        create_server(rest_mock)
    ftp_mock = get_server("FTP_MOCK_SERVER")
    if ftp_mock is None:
        ftp_mock = Server(
            str(uuid.uuid4()), 
            "FTP_MOCK_SERVER", 
            "FTP", 
            Config("localhost", "user", "123").__dict__,
            datetime.now(timezone.utc))
        create_server(ftp_mock)

def get_rest(server):
    return get_companies_info(server.config)

def get_ftp(server):
    files = get_files_names(server.config)
    reports = []
    for file in files:
        report = get_file_data(server.config, file)
        reports += report['companies']
    return {
        "companies": reports
    }