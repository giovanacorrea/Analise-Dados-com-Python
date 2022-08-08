#alterar números impares para -1 
import numpy as np 

data = np.arange(10)
#antes sem a alteração
print(data)

#depois da alteração
data[data%2 != 0] = -1
print(data)