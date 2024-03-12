import pika
import json
from ..infraestructura.dto import AddCompanyMessage
 
def send_company_data(company):
    print("Hola Mundo")
    print(company)
    company_message = AddCompanyMessage(company.name, company.age, company.description, company.address)
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='company_created')
    channel.basic_publish(exchange='',
                        routing_key='company_created',
                        body=json.dumps(company_message.__dict__))
    print(" ", end="")
    connection.close()