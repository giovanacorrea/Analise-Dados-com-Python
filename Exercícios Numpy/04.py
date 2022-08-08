#criar um array de 0 a 9 e printar apenas os números ímpares 
import numpy as np 

data = np.arange(10)
ans = data[data%2 != 0]
print(ans)