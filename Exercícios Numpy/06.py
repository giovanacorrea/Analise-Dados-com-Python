#Replace all odd numbers in arr with -1 without changing arr
import numpy as np 

data = np.arange(10)
#A função where faz a operação lógica if(par) = True, entao guarda o num else coloca -1 
ans = np.where(data%2 != 0, -1, data)

ans
