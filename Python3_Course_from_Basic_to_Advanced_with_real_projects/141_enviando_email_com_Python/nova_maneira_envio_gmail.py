import smtplib
import email.message


def enviar_email():
    corpo_email = """
    <p>Oi!</p>
    <p>Tudo bem!</p>
    """

    msg = email.message.Message()
    msg['Subject'] = "Assunto"
    msg['From'] = 'wmarenga44@gmail.com'
    msg['To'] = 'wmarenga@yahoo.ca'
    password = '12345'
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email)

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Login Credentials for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email enviado com sucesso!!!')


enviar_email()
