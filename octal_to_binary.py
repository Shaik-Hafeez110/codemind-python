n=int(input())
b=0
d=0
j=0
while(n):
    i=n%10
    d=d+i*(8**j)
    j+=1
    n=n//10
i=1
while(d):
    b=b+(d%2)*i
    i*=10
    d=d//2
print(b)    
    
    