import pika
import json
class MailService():

    def __init__(self):
        self.connection = None
        self.channel = None
        self.connect()
        self.consume()

    def callback(self,ch,method,properties,body):
        print(json.loads(body)['emails'])

    def consume(self):
        self.channel.start_consuming()

    def connect(self):
        #Conexión RabbitMQ
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        self.channel=self.connection.channel()
        #Crear consumo
        self.channel.basic_consume(self.callback,queue='Mailing',no_ack=True)

mail = MailService()