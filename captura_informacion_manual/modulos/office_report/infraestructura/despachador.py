import pika
import json
from .dto import OfficeReportMessage 

def event_office_report_create(officereport):
    office_message = OfficeReportMessage(officereport.id, officereport.direccion, officereport.oficinas, officereport.banos, officereport.descripcion)    
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='office_report_created')
    channel.basic_publish(exchange='',
                        routing_key='office_report_created',
                        body=json.dumps(office_message.__dict__))
    print(" ", end="")
    connection.close()