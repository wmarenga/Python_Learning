from socket import timeout
from string import Template
from datetime import datetime

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import smtplib

meu_email = 'wmarenga44@gmail.com'
minha_senha = '1234'

with open('141_enviando_email_com_Python/template.html', 'r', encoding='utf8') as html:
    template = Template(html.read())
    data_atual = datetime.now().strftime('%d/%m/%Y')
    corpo_msg = template.substitute(nome='Wellington Marenga', data=data_atual)

msg = MIMEMultipart()
msg['from'] = 'Wellington Marenga'
msg['to'] = 'wmarenga44@gmail.com'  # Cliente
msg['subject'] = 'Atenção este é um email de teste!!'

corpo = MIMEText(corpo_msg, 'html')
msg.attach(corpo)

# ENVIO DE IMAGEM EM ANEXO
# with open('141_enviando_email_com_Python/IMAGEM.JPG', 'rb') as img:
#    img = MIMEImage(img.read())
#    msg.attach(img)

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    try:
        smtp.ehlo()
        smtp.starttls()
        smtp.login(meu_email, minha_senha)
        smtp.send_message(msg)
        print('E-mail enviado com sucesso.')
    except Exception as e:
        print('E-mail não enviado...')
        print('Erro:', e)
