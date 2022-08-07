import math 
#encontrar quantos jogadores estão no range da standard deviation
players = [180, 172, 178, 185, 190, 195, 192, 200, 210, 190]
cont = 0.0

tam = len(players)

#Calcula a média de alturas
for x in players :
    cont+=x   
mean = cont/tam

#calcula a variancia
variance = 0.0
for y in players :
    variance += ((y-mean)**2)/tam

#standard variation = raiz quadrada da variância 
sd = math.sqrt(variance)
ans = 0

#contamos quantos jogadores estão no range da diferença de uma variância da média 
for p in players :
   if(p>=(abs(mean-sd)) and p<=(mean+sd)) :
    ans+=1
 

#print(sd)
print(ans)
#print('{:.4f}'.format(mean))