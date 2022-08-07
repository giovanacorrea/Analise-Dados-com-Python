#Exercício para utilizar funções append e sort da numpy

import numpy as np

data = np.array([1000, 2500, 1400, 1800, 900, 4200, 2200, 1900, 3500])

Newhouse = int(input())

data = np.append(data, Newhouse)
data = np.sort(data)
print(data)