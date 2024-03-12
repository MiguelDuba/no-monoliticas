import pika,json
from ..application.comandos.saga_massive_reports import iniciar

def traer_informacion_masiva(ch, method, properties, body):
    iniciar()

def suscribirse_a_consultar_masiva_servers():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='traer_informacion_server')

    channel.basic_consume(queue='traer_informacion_server', on_message_callback=traer_informacion_masiva, auto_ack=True)

    print(' [*] Waiting for messages from traer_informacion_server. To exit press CTRL+C')
    channel.start_consuming()