import matplotlib.pyplot as plt
import numpy as np

#questão 5 lista 02
recebidos = [160, 184, 241, 149, 180, 161, 132, 202, 160, 139, 149, 177]
processados = [160, 184, 237, 148, 181, 150, 123, 156, 126, 104, 124, 140]
mes = ['Jan', 'Fev', 'Mar', 'Abr', 'Maio', 'Jun', 'Jul', 'Ago','Set','Out','Nov','Dez']

x1 =  np.arange(len(recebidos))
#print(x1)

x2 = [x + 0.25 for x in x1]

#print(x2)

plt.bar(x1, recebidos, width=0.25, label = 'Recebidos', color = 'g')
plt.bar(x2, processados, width=0.25, label = 'Processados', color = 'r')
plt.xticks([x + 0.25 for x in range(len(recebidos))], mes)
plt.title("Gráfico de recebidos e processados")
plt.ylabel("Quantidade")
plt.legend()
plt.show()

