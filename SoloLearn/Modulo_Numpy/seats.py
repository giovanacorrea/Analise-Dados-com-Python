import numpy as np

import numpy as np

data = np.array([1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0])

#transforma o array em uma matriz 6x5 
data = data.reshape(6,5)

#Pega o número da linha dado para o usuário e printa 
row = int(input())
print(data[row])

