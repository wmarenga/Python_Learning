"""
Manipulando Data e Hora

Python tem um módulo built-in (integrado) para se trabalhar com data e hora
chamado datetime.

import datetime

print(dir(datetime))

['MAXYEAR', 'MINYEAR', '__all__', '__builtins__', '__cached__', '__doc__',
 '__file__', '__loader__', '__name__', '__package__', '__spec__', 'date',
 'datetime', 'datetime_CAPI', 'sys', 'time', 'timedelta', 'timezone',
 'tzinfo']

2018-12-21 15: 36: 38.056382

2018-12-21 15: 41: 38.056382

print(datetime.MAXYEAR)

print(datetime.MINYEAR)


# Retorna a data e hora corrente

print(datetime.datetime.now())  # 2018-12-21 15:36:38.056382   BR 21/12/2018


# datetime.datetime(year, month, day, hour, minute, second, microsecond)

print(repr(datetime.datetime.now()))


# replace() para fazer ajustes na data/hora

inicio = datetime.datetime.now()

print(inicio)

# Alterar o horário para 16 horas, 0 minuto, 0 segund, 0 microsegundo
inicio = inicio.replace(year=2023, hour=16, minute=0, second=0, microsecond=0)

print(inicio)

# Recebendo dados do usuário e convertendo para data (criar)

evento = datetime.datetime(2019, 1, 1,0)

print(type(evento))

print(type('31/12/2018'))

print(evento)

# Convertendo dados do usuário para data Python (datetime)
nascimento = input('Informa sua data de nascimento (dd/mm/yyy): ')

print(type(nascimento)) # <class 'str'> => '15/07/1999'

nascimento = nascimento.split('/') # Cria uma lista de strings e as separa
                                    pela barra. ['15', '07', '1999']

# nascimento[2] => 1999 (ano); nascimento[1] => 07(mês); nascimento[0]) => 15 (dia)
# Convertendo para inteiro
nascimento = datetime.datetime(
    int(nascimento[2]), int(nascimento[1]), int(nascimento[0]))

print(nascimento)

print(type(nascimento))

# Acessa individual dos elementos de data e hora (retorna um número inteiro)

import datetime

evento = datetime.datetime.now()

print(evento.year)  # ano
print(type(evento.year)) # Retorna um númeroi inteiro
print(evento.month)  # mês
print(evento.day)  # dia
print(evento.hour)  # hora
print(evento.minute)  # minuto
print(evento.second)  # segundo
print(evento.microsecond)  # microsegundo

print(dir(evento))
"""
