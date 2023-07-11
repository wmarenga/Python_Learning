""" 
O que e otimizacao?

- Busca pela decisao otima;
- Qualquer problema de planejamento: longo, medio, curto prazo, operacional;
- Aplicando a decisao de investimento, operacao, definicao de rotas, reducao de custos... 
- Ex.: Desejamos maximizar a receita da venda de 2 produtos (x e y), sendo que cada um
custa 1 real. Qual a producao diaria necessaria?

Programacaos linear

Conhecendo as seguintes restricoes de operacao:
2y     <= x + 8 (tempo de producao)
2x + y <= 14 (materia prima)
2x     <= y + 10 (historico de venda)
x, y   <= 10 (maximo diario)

Output:

Programacaos linear

max x + y
-x + 2y <= 8
2x + y <= 14
2x - y <= 10
0 <= x <= 10
0 <= y <= 10

Programacaos nao linear

2y     <= x + 8 (tempo de producao)
x (2 + y) <= 14 (materia prima) --> com esta restricao transformariamos em nao linear
2x     <= y + 10 (historico de venda)
x, y   <= 10 (maximo diario)

Output:

Programacaos nao linear

max x + y
-x + 2y <= 8
2x + yx <= 14 (restricao)
2x - y <= 10
0 <= x <= 10
0 <= y <= 10

* Se tivessemos uma definicao de que x e y sao inteiros, uma programacao linear inteira mista poderia resolver o problema. 

Etapas:
Entendimento do Problema ==> Modelagem ==> Resolucao ==> Resultados ==>

"""