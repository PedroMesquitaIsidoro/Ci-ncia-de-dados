import pandas as pd
import matplotlib.pyplot as plt
### histograma v1

dados = [51, 53, 56, 58, 59, 59, 60, 64, 65, 68, 69, 73, 74, 75, 76, 77, 77, 78, 79, 79]

def histograma(dados, caixas):
  plt.hist(dados, bins = caixas, width = 1)
  plt.ylabel("Frenquência")
  plt.xlabel("Dados")
  plt.show()

#amplitude 79 - 51 = 28

histograma(dados, 28)
