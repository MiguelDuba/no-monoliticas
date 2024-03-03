import uuid
from datetime import datetime, timezone 
from out.adapter.rest.companies_call import get_companies_info
from out.adapter.db.postgres import save_records

def start_companies_check(ch, method, properties, body):
    print(f" [x] Received {body}")
    companies_report = get_companies_info()
    report = {
        "id": str(uuid.uuid4()),
        "companies_list": companies_report,
        "create_date": datetime.now(timezone.utc)
    }
    print(report)
    save_records(report)
    