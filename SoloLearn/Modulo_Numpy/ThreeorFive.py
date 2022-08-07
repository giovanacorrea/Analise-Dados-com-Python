import numpy as np

#Cria o array e preenche no intervalo de 1 a 101 e printa apenas os números múltiplos de 3 e 5  
data = np.arange(1, 101)
print(data[(data%3 == 0) & (data%5==0)])
