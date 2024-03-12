import pika,json, sys,os

def mostrar_mensaje_recivido(ch, method, properties, body):
        print(f" [x] Received {body}")

def start_listen_for_companies():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='company_report_created')

    channel.basic_consume(queue='company_report_created', on_message_callback=mostrar_mensaje_recivido, auto_ack=True)

    print(' [*] Waiting for messages from company_report_created. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == '__main__':
    try:
        start_listen_for_companies()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)