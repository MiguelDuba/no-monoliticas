import pika,json
from ..applicacion.comandos.consultar_servidor import consultar_servidor_compania
from ..applicacion.comandos.consultar_servidor import ConsultarCompaniaServidor

def traer_informacion_company_server(ch, method, properties, body):
    body = json.loads(body)
    print(f'Message {body}')
    consultar_servidor = ConsultarCompaniaServidor(None,body['name'])
    consultar_servidor_compania(consultar_servidor)



def suscribirse_a_consultar_servidor_compania():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='traer_informacion_company_server')

    channel.basic_consume(queue='traer_informacion_company_server', on_message_callback=traer_informacion_company_server, auto_ack=True)

    print(' [*] Waiting for messages from traer_informacion_company_server. To exit press CTRL+C')
    channel.start_consuming()


def mostrar_mensaje_recivido(ch, method, properties, body):
        print(f" [x] Received {body}")

def start_listen_for_companies():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='company_report_created')

    channel.basic_consume(queue='company_report_created', on_message_callback=mostrar_mensaje_recivido, auto_ack=True)

    print(' [*] Waiting for messages from mostrar_mensaje_recivido. To exit press CTRL+C')
    channel.start_consuming()