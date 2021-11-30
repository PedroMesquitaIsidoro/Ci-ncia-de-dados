import pandas as pd
import matplotlib.pyplot as plt
### histograma v1

dados = [20, 21, 21, 22, 22, 23, 23, 23, 24, 24, 24, 25, 26, 27, 28, 29, 29, 29, 30, 30]

def histograma(dados, caixas):
  plt.hist(dados, density=False, bins = caixas, width = 1)
  plt.ylabel("Frenquência")
  plt.xlabel("Dados")
  plt.show()

#NÚMERO DE BARRAS: (30 - 20)/ 1 = 10

histograma(dados, 10)
