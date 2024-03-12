import pika
import json

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='traer_informacion_catrastal_server')
body = {
    "name": "FTP_MOCK_SERVER"
}
channel.basic_publish(exchange='',
                      routing_key='traer_informacion_catrastal_server',
                      body=json.dumps(body))
print(" [x] Sent 'start check cadastral'")
connection.close()