import uuid
from datetime import datetime, timezone 
from core.domain.report import CompanyReport, Report
from out.adapter.rest.companies_call import get_companies_info
from out.adapter.db.postgres import save_records
from out.adapter.produccer.send_company_info import send_company_report

def start_companies_check(ch, method, properties, body):
    print(f" [x] Received {body}")
    companies_report = get_companies_info()
    report = Report(str(uuid.uuid4()), companies_report["companies"], datetime.now(timezone.utc))
    print(f"Record to create {report.id} with {len(report.companies_list)} with date {report.created_date}")
    save_records(report)
    for company in report.companies_list:
        company_report = CompanyReport(report.id, 
                                       company["name"],
                                       company["age"],
                                       company["description"],
                                       company["address"],
                                       report.created_date.strftime("'%Y-%m-%dT%H:%M:%SZ"))
        print(f"Compay Record to send {company_report.report_id} for {company_report.name} with date {company_report.created_date}")
        send_company_report(company_report.__dict__)