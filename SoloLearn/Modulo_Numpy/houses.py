#verifica a porcentagem de casas com preço a uma standard deviation da média
import numpy as np

data = np.array([150000, 125000, 320000, 540000, 200000, 120000, 160000, 230000, 280000, 290000, 300000, 500000, 420000, 100000, 150000, 280000])

sd = np.std(data)
mean = np.mean(data)
ans=0
tam = len(data)

for p in data :
   if(p>=(abs(mean-sd)) and p<=(mean+sd)) :
    ans+=1
 
res = (ans/tam)*100

print(res)
