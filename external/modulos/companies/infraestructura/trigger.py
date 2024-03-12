import pika
import json

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='traer_informacion_company_server')
body = {
    "name": "REST_MOCK_SERVER"
}
channel.basic_publish(exchange='',
                      routing_key='traer_informacion_company_server',
                      body=json.dumps(body))
print(" [x] Sent 'start check companies'")
connection.close()