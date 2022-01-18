import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from statsmodels.tsa.seasonal import seasonal_decompose
from dateutil.parser import parse

#questão 07 lista 2
#carregar do hitgub
link = 'https://raw.githubusercontent.com/bapimentel/Ciencia-de-Dados/master/Dados/Drugs.csv'
df = pd.read_csv(link, parse_dates=['date'], index_col='date')

#Decomposição aditiva
result_add = seasonal_decompose(df['value'], model='additive', extrapolate_trend='freq')

#Plot
plt.rcParams.update({'figure.figsize': (10,10)})
result_add.plot().suptitle('Additive Decompose', fontsize=22)
plt.show()
