vac_nums = [0,0,0,0,0,1,1,1,1,1,1,1,1,2,2,2,2,3,3,3]
#your code goes here

cont=0.0
cont0=0.0

for x in vac_nums :
    if(x>=1) :
        cont+=x
    
ans = cont/20.0
print('{:.2f}'.format(ans))
