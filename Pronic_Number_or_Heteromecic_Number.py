a=int(input())
i=1
f=0
while(i<a//2):
    if(a==i*(i+1)):
        f=1
        print("YES")
        break
    else:
        i+=1
if(f==0):
    print('NO')
