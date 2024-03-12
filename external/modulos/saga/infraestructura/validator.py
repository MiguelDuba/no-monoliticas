import pika,json, sys,os

def mostrar_mensaje_recivido(ch, method, properties, body):
        print(f" [x] Received {body}")

def start_listen_for_companies():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='massive_report_fail')

    channel.basic_consume(queue='massive_report_fail', on_message_callback=mostrar_mensaje_recivido, auto_ack=True)

    print(' [*] Waiting for messages from massive_report_fail. To exit press CTRL+C')
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