""" 
Qual solver e framework escolher?

*** AML => Linguagem de modelagem algebrica

   Framework    |  Problemas |  Problemas     |  Facilidade  |  Facilidade de Configurar  |  Facilidade de    |
     (AML)      |  Lineares  |  Nao Lineares  |  de Iniciar  |  um novo solver            |  troca de solver  |
----------------|------------|----------------|--------------|----------------------------|-------------------|
    Pyomo       |      X     |       X        |     Media    |           Alta             |       Alta        |
    OrTools     |      X     |                |  Muito Alta  |           Baixa            |       Alta        |
    PuLP        |      X     |                |      Alta    |           Alta             |       Media       |
    SCIP        |      X     |       X        |      Alta    |       Nao e Possivel       |  Nao e Possivel   |
    SciPy       |      X     |       X        |      Baixa   |           Media            |       Media       |
    
Pyomo ==> Nao tao simple de se trabalhar no inicio, contudo e o mais indicado, pois ele trabalha com programacao linear e nao linear. Simples integracao com outros solvers.
Or-Tools ==> Simples e didatico, porem so trabalha com programacao linear assim como PuLP.

     Solver     |  Problemas |  Problemas     |     Gratis/    |
                |  Lineares  |  Nao Lineares  |    Comercial   |
----------------|------------|----------------|----------------|
    Gurobi      |      X     |                |    Comercial   |
    Cplex       |      X     |                |    Comercial   |
    CBC         |      X     |                |     Gratis     |
    GLPK        |      X     |                |     Gratis     |
    IPOPT       |            |       X        |     Gratis     |
    SCIP        |      X     |       X        |     Gratis     |
    Baron       |            |       X        |    Comercial   |

Precisamos entender primeiramente a natureza do problema:

>> Problema Linear ou Linear inteiro misto => os indicados seriam o Gurobi ou Cplex, pois sao os mais conceitudos no tema
e resolvem problemas de larga escala da industria. 
>> Se estiver apenas iniciando no tema ==> O indicado e utilizar o CBC e GLPK, pois sao gratis e resolvem problemas de media
e larga escala razoavelmente.
>> Problemas Nao Lineares ==> O recomendado seria utilizar os gratis (IPOPT e SCIP). IPOPT e indicado para problemas nao lineares
somente (nao indicado para problemas com variaveis inteiras). O IPOPT trabalha tambem com metodos pontos interiores.
>> Um Solver excelente para trabalhar com problemas de altissima complexidade e nao lineares e com variaveis inteiras. Solver adequado
para resolver problemas inteiro misto nao lineares. Ele tem altissima performance.

"""