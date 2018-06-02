# MailService
 #Table of Contents

* [Uso](#Uso)

<a name="installation"></a>
# Uso

## Prerequisitos

- Python version 3.6
## Crear Variables de antorno


```bash
echo "export SENDGRID_API_KEY='YOUR_API_KEY'" > sendgrid.env
echo "sendgrid.env" >> .gitignore
source ./sendgrid.env
```

## Dependencias

- [SendGrid-Python](https://github.com/sendgrid/sendgrid-python)
- [pika](https://github.com/pika/pika)
