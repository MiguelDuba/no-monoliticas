import json
from config.postgres import get_cursor

def save_company_report(company_report):
    cursor = get_cursor()
    query = """ insert into company_report(id, companies_list, server_name, status, created_date) VALUES (%s, %s, %s,%s,%s) """
    cursor.execute(query, (company_report.id, json.dumps(company_report.companies_list), company_report.server_name, company_report.status, company_report.created_date))

def update_company_report_status(company_report):
    cursor = get_cursor()
    query = """ update company_report SET status = %s where id = %s """
    cursor.execute(query, (company_report.staus, company_report.status))