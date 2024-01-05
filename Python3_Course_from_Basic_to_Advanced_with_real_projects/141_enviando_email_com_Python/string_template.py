from string import Template
from datetime import datetime
from dados_email.login import email, senha

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import smtplib  # entra no servidor para enviar a msg

with open('140_string_template/template.html', 'r', encoding='utf8') as html:
    template = Template(html.read())
    data_atual = datetime.now().strftime("%d/%m/%Y")
    # Tem que ter a mesma quantidade de parâmetros nomeados do html
    corpo_msg = template.substitute(nome='Wellington Marenga', data=data_atual)
    # usando o safe_substitute, será ignorado algum parametro que não foi citado ($outro)
    # corpo_msg = template.safe_substitute(nome='Luiz Otávio', data=data_atual)

msg = MIMEMultipart()
msg['from'] = 'wmarenga44@gmail.com'
msg['to'] = 'wmarenga@yahoo.ca'  # email do cliente
msg['subject'] = 'Atenção: este é um e-mail de teste.'

corpo = MIMEText(corpo_msg, 'html')
msg.attach(corpo)

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(email, senha)
    smtp.send_message(msg)
    print('E-mail enviado com sucesso.')

    # O <strong> do html, deixa o texto em negrito.
print(corpo_msg)
