import pika
import json
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel=connection.channel()
channel.queue_declare(queue='Mailing')
test = {
  "emails": [
    "test1@gmail.com"
  ],
  "cc":[
    "test4@gmail.com",
    "test2@gmail.com",
    "test3@gmail.com"
  ],
  "subject": "the subject",
  "values": {
    "Name": "Juan",
    "cc": "100000",
    "lastname": "Sosa"
  },
  "template": "test"
}
channel.basic_publish(exchange='',routing_key='Mailing', body = json.dumps(test))
print(test['values'].keys())
for x in test['values'].keys():
  print (x,test['values'][x])
