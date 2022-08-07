import statistics
import math

vac_nums = [0,0,0,0,0,1,1,1,1,1,1,1,1,2,2,2,2,3,3,3]
cont = 0.0

#Calcula a média de vacinações
for x in vac_nums :
    cont+=x   
mean = cont/20.0

#calcula a variancia que é a (média de vacinações - vacinação individual^2)
variance = 0.0
for y in vac_nums :
    variance += ((y-mean)**2)/20.0

print('{:.4f}'.format(variance))

