import pika
from core.service.companies_service import start_companies_check

def start_listen_for_companies():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='company')

    channel.basic_consume(queue='company', on_message_callback=start_companies_check, auto_ack=True)

    print(' [*] Waiting for messages from company. To exit press CTRL+C')
    channel.start_consuming()