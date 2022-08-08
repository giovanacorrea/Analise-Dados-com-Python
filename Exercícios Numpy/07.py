#Converter um array de tamanho dez de 1 dimensão para um de 2 dimensões
import numpy as np 
data = np.arange(10)
data = data.reshape(2,5)

print(data)