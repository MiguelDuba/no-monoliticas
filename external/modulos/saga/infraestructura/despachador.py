import pika
import json
from .dto import MassiveReportError

def evento_massive_report_fail(id, server, step):
    message = MassiveReportError(id, step, server)
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='massive_report_fail')
    channel.basic_publish(exchange='',
                        routing_key='massive_report_fail',
                        body=json.dumps(message.__dict__))
    connection.close()