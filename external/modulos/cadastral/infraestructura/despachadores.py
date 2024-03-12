import pika
import json

def evento_cadastral_report_created(cadastral_report):
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='cadastral_report_created')
    channel.basic_publish(exchange='',
                        routing_key='cadastral_report_created',
                        body=json.dumps(cadastral_report))
    connection.close()