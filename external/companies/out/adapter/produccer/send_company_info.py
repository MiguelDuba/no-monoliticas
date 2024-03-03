import pika
import json

def send_company_report(report):
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='company_report')
    channel.basic_publish(exchange='',
                        routing_key='company_report',
                        body=json.dumps(report))
    print(" [x] Sent 'Send company information report'")
    connection.close()