from string import Template
from datetime import datetime

with open('140_string_template/template.html', 'r', encoding='utf8') as html:
    template = Template(html.read())
    data_atual = datetime.now().strftime("%d/%m/%Y")
    # Tem que ter a mesma quantidade de parâmetros nomeados do html
    corpo_msg = template.substitute(nome='Luiz Otávio', data=data_atual)
    # usando o safe_substitute, será ignorado algum parametro que não foi citado ($outro)
    # corpo_msg = template.safe_substitute(nome='Luiz Otávio', data=data_atual)

# O <strong> do html, deixa o texto em negrito.
print(corpo_msg)
