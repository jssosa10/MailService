import sendgrid
import os
#from htmlmapper import *
from sendgrid.helpers.mail import *

sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))
class Sender():
    def sendMail(self,emails,cc,sub,template,values):
        data = self.buildMail(emails,cc,sub,template,values)
        response = sg.client.mail.send.post(request_body=data)
        print(response.status_code)
        print(response.headers)
        print(response.body)
    def buildMail(self,emails,cc,sub,template,values):
        from_email = Email("test@example.com")
        subject = sub
        to_email = Email(emails[0])
        content = Content("text/plain", "some text here")
        mail = Mail(from_email, subject, to_email, content)
        for i in range(1,len(emails)):
            mail.personalizations[0].add_to(Email(emails[i]))
        for x in cc:
            mail.personalizations[0].add_cc(Email(x))
        return mail.get()
