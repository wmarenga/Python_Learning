import pandas as pd
import numpy as np
import copy

tabela = pd.DataFrame({'nome':['rafael','joao','rafael','maria'], 'nota':[10,9,8,7]})

tabela2 = np.array(tabela)

tabela3 = copy.deepcopy(tabela)

tabela3.loc[0,'nota'] = 3