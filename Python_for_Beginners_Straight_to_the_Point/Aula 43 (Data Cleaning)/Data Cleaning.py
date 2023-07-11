"""
Data Cleaning (Etapas do processo):
- Lidar com dados nulos;
- Busca por Outliers (dados que nao parecem fazer parte do conjunto de dados) e tratativas;
- Busca por inconsistencias entre bases (ex. alguma venda para cliente inexistente?);
- Busca por dados duplicados;
- Tratativas com formato de dados (ex.: datas);
- Identificacao de chave primaria;
- Normalizacao?

O que devemos avaliar?
- Entender o contexto dos dados;
- Se existem dados fora do padrao;
- Entender porque a base e inconsistente e fazer a tratativas necessarias;

Possiveis cenarios na limpeza de dados:
- Erros de digitacao (digitado 100 mas era 10) - falha humana;
- Sensor descalibrado, quebrado ou intermitente;

Etapas na avalicao dos dados:
1) Procurar por dados nulos e tratamos estes dados;
2) Procuramos por Outliers, dados que nao parecem fazer parte do nosso conjunto de dados;
3) Procuramos por inconsistencias na base. Ex. Venda gerada para cliente ou loja inexistente;
4) Buscamos por dados duplicados (podem poluir as nossas analises);
5) Procuramos por inconsistencias nos formatos de datas e nomeros;
6) Identificar a chave primaria das bases, esta chave estabelece uma ligacao entre as bases,
esta chave tem que ser unica, pois sera uma referencia entre as bases. 
7) Algumas pessoas preferem normalizar os dados, colocando todos os dados em uma escala comum.
"""