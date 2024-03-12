import pika
from ...dominio.servicios import add_companies_service


def start_listen_for_companies():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='company_created')

    channel.basic_consume(queue='company_created', on_message_callback=add_companies_service, auto_ack=True)

    print(' [*] Waiting for messages from company. To exit press CTRL+C')
    channel.start_consuming()