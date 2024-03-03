import pika
from core.service.companies_service import start_companies_check

def start_listen_for_companies():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='hello')

    channel.basic_consume(queue='hello', on_message_callback=start_companies_check, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()