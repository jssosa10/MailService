import pika
import json
import sendMails
class MailService():

    def __init__(self):
        self.sender = sendMails.Sender()
        self.connection = None
        self.channel = None
        self.connect()
        self.consume()

    def callback(self,ch,method,properties,body):
        parameters = json.loads(body)
        self.sender.sendMail(parameters['emails'],parameters['cc'],parameters['subject'],parameters['template'],parameters['values'])

    def consume(self):
        self.channel.start_consuming()

    def connect(self):
        #Conexión RabbitMQ
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        self.channel=self.connection.channel()
        #Crear consumo
        self.channel.basic_consume(self.callback,queue='Mailing',no_ack=True)

mail = MailService()