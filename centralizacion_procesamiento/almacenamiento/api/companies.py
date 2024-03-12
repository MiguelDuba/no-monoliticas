import pika
from core.services.companies_services import guardar_info_companias

def start_listen_for_companies():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='company_created')

    channel.basic_consume(queue='company_created', on_message_callback=guardar_info_companias, auto_ack=True)

    print(' [*] Waiting for messages from company. To exit press CTRL+C')
    channel.start_consuming()