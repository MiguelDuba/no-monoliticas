import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='company')
channel.basic_publish(exchange='',
                      routing_key='company',
                      body='start check companies')
print(" [x] Sent 'start check companies'")
connection.close()