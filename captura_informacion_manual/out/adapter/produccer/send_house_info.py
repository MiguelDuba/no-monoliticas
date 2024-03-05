import pika
import json

def send_house_data(house):
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='house_created')
    channel.basic_publish(exchange='',
                        routing_key='house_created',
                        body=json.dumps(house))
    print(" ", end="")
    connection.close()