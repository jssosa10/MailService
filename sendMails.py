import sendgrid
import os
import htmlmapper
from sendgrid.helpers.mail import *
from Exceptions import *

"""
    Clase encargada de enviar correos usando sendgrid
"""
class Sender():
    def __init__(self):
        self.sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))
        self.mapper = htmlmapper.HtmlMapper()
    """
        Funación encargada de enviar correos
    """
    def sendMail(self,emails,cc,sub,template,values):
        try:
            data = self.buildMail(emails,cc,sub,template,values)
            response = self.sg.client.mail.send.post(request_body=data)
            print(response)
            return response.status_code
        except IncompleteValuesException:
            return 500
    """
        Función encargada de construir el mensaje utilizando los parametros especificados
    """
    def buildMail(self,emails,cc,sub,template,values):
        from_email = Email("test@example.com")
        subject = sub
        to_email = Email(emails[0])
        try:
            content = Content("text/html", self.mapper.map(template,values))
            mail = Mail(from_email, subject, to_email, content)
            for i in range(1,len(emails)):
                mail.personalizations[0].add_to(Email(emails[i]))
            for x in cc:
                mail.personalizations[0].add_cc(Email(x))
            return mail.get()
        except IncompleteValuesException:
            #print('Error con los datos reqeridos')
            raise IncompleteValuesException('Error de datos')
