import scipy.stats as stats
# os dados v1 e v2
v1 = [19, 19, 20, 20, 21, 22, 22, 23, 24, 25, 26, 26, 27, 29, 29, 29, 29, 30, 30, 30]
v2 = [51, 53, 56, 58, 59, 59, 60, 64, 65, 68, 69, 73, 74, 75, 76, 77, 77, 78, 79, 79]

def teste(dados):
  shapiro_stat, shapiro_p_valor = stats.shapiro(dados)
  print("O valor calculado do teste de Shapiro-Wilk eh de = " + str(shapiro_stat))
  print("O p-valor calculado para o teste de Shapiro-Wilk eh de = " + str(shapiro_p_valor))
  if shapiro_p_valor >= 0.05:
      print("Dados seguem uma distribuicao normal")
  else:
      print("Dados não seguem uma distribuicao normal")
print("Pra v1:")
teste(v1)
print("\nPra v2:")
teste(v2)
