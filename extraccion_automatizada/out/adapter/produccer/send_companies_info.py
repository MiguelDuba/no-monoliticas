import pika
import json
 
def send_company_data(company):
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='company_created')
    channel.basic_publish(exchange='',
                        routing_key='company_created',
                        body=json.dumps(company))
    print(" ", end="")
    connection.close()