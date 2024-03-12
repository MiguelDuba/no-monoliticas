import pika,json
from ..applicacion.comandos.consultar_servidor import consultar_servidor_catrastal
from ..applicacion.comandos.consultar_servidor import ConsultarCatastralServidor

def traer_informacion_cadastral_server(ch, method, properties, body):
    body = json.loads(body)
    print(f'Message {body}')
    consultar_servidor = ConsultarCatastralServidor(None, body['name'])
    consultar_servidor_catrastal(consultar_servidor)



def suscribirse_a_consultar_servidor_catrastal():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='traer_informacion_catrastal_server')

    channel.basic_consume(queue='traer_informacion_catrastal_server', on_message_callback=traer_informacion_cadastral_server, auto_ack=True)

    print(' [*] Waiting for messages from traer_informacion_catrastal_server. To exit press CTRL+C')
    channel.start_consuming()
