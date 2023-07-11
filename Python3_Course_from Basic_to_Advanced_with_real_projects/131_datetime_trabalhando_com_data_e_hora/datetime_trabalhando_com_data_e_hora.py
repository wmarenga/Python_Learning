"""
https://docs.python.org/3.10/library/datetime.html
"""
from datetime import datetime, timedelta, timezone
from time import strftime

"""
# datetime(ano, mês, dia, hora => opcional, minuto => opcional, segundo => opcional)
data = datetime(2019, 4, 10, 10, 53, 20)
print(data)
# formatando a data usando as diretivas (ver documentação).
print(data.strftime('%d/%m/%Y %H:%M:%S'))

# Converte uma string em uma data .strptime('string', 'formato')
data = datetime.strptime('20/04/2019',  '%d/%m/%Y')
print(data)

# timestamp é contagem de segundos desde 1970
print(data.timestamp())

# Converter uma data pelo timestamp
data2 = datetime.fromtimestamp(1555711200.0, timezone.utc)
print(data2)

data = datetime.strptime('20/04/1987 20:00:00', '%d/%m/%Y %H:%M:%S')
# data = data + timedelta(days=5, seconds=59)
# Poderíamos fazer cálculos com os segundos
data = data + timedelta(seconds=2*60*60)  # 2 horas a mais
data = data + timedelta(seconds=59*60)  # 59 minutos a mais
print(data, strftime('%d/%m/%Y %H:%M:%S'))
"""
# Comparação de datas
d1 = datetime.strptime('20/04/1987 20:00:00', '%d/%m/%Y %H:%M:%S')
d2 = datetime.strptime('25/04/1987 22:33:00', '%d/%m/%Y %H:%M:%S')

dif = d2 - d1
print(dif)
print(dif.seconds)  # somente os segundos (somente da hora)
print(dif.total_seconds())  # Os segundos totais (dias e horas)
print(dif.days)  # somente a quantidade de dias

print(d1.time())  # somente a hora

print(d1 < d2)  # comparação entre datas
