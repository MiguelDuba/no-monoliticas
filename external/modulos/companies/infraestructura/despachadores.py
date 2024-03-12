import pika
import json

def evento_company_report_created(company_report):
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='company_report_created')
    channel.basic_publish(exchange='',
                        routing_key='company_report_created',
                        body=json.dumps(company_report))
    connection.close()

def evento_mock_solicitar_report_compania():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='company')
    body = {
        "name": "FTP_MOCK_SERVER"
    }
    channel.basic_publish(exchange='',
                        routing_key='company',
                        body=json.dumps(body))
    print(" [x] Sent 'start check companies'")
    connection.close()