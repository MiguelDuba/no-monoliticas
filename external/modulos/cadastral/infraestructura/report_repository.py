import json
from config.postgres import get_cursor

def save_cadastral_report(cadastral_report):
    cursor = get_cursor()
    query = """ insert into cadastral_report(id, houses_list, server_name, status, created_date) VALUES (%s, %s, %s, %s, %s) """
    cursor.execute(query, (cadastral_report.id, json.dumps(cadastral_report.houses_list), cadastral_report.server_name, cadastral_report.status, cadastral_report.created_date))

def update_cadastral_report_status(cadastral_report):
    cursor = get_cursor()
    query = """ update cadastral_report SET status = %s where id = %s """
    cursor.execute(query, (cadastral_report.staus, cadastral_report.status))