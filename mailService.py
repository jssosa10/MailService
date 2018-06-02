import pika
import json
import configparser, json
import sendMails
from Exceptions import *
"""
    Clase encargada de realizar comunicación con RabbitMQ
"""
class MailService():
    def __init__(self):
        config = configparser.ConfigParser()
        config.read('config.cfg')
        self.sender = sendMails.Sender()
        self.connection = None
        self.channel = None
        self.host=config.get('MQ', 'host')  
        self.queue=config.get('MQ', 'queue')
        print (self.host)
        print (self.queue)
        self.connect()
        self.consume()
    """
        Función encargada de realizar acciones apenas llega un mensaje a RabbitMQ
    """
    def callback(self,ch,method,properties,body):
        parameters = json.loads(body)
        code = self.sender.sendMail(parameters['emails'],parameters['cc'],parameters['subject'],parameters['template'],parameters['values'])
        print(code)
        if code==202:
            print('correo enviado')
        else :
            print('no se envio el correo con la siguiente información %s',parameters)
    """
        Funación encargada de cconsumir de RabbitMQ
    """
    def consume(self):
        self.channel.start_consuming()

    """
        Función encargada de realizar la conexión con RabbitMQ
    """
    def connect(self):
        #Conexión RabbitMQ
        try:
            self.connection = pika.BlockingConnection(pika.ConnectionParameters(host=self.host))
            self.channel=self.connection.channel()
            #Crear consumo
            self.channel.basic_consume(self.callback,queue=self.queue,no_ack=True)
        except:
            print("No fue posible realizar conexión revise los parametros.")

mail = MailService()