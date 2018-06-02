# MailService
# Table of Contents

* [Uso](#Uso)
* [Descripción](#Descripción)
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

# Descripción

Servicio encargado de enviar un correo usando cierto parametros y editando un template HTML que sera el cuerpo del correo.
