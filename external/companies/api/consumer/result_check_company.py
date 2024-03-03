import pika
import sys, os

def callback(ch, method, properties, body):
        print(f" [x] Received {body}")

def start_listen_for_companies():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='company_report')

    channel.basic_consume(queue='company_report', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages from company_report. To exit press CTRL+C')
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