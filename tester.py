import pika
import json
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel=connection.channel()
channel.queue_declare(queue='Mailing')
test = {
  "emails": [
    "test@gmail.com",
    "test2@gmail.com",
    "test3@gmail.com"
  ],
  "cc":[
    "test@gmail.com",
    "test2@gmail.com",
    "test3@gmail.com"
  ],
  "subject": "the subject",
  "values": {
    "var1": "value of var1",
    "var2": "value of var2",
    "var3": "value of var3"
  },
  "template": "name of templete (HTML)"
}
channel.basic_publish(exchange='',routing_key='Mailing', body = json.dumps(test))
