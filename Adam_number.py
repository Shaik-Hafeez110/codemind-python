a=int(input())
s=0
reva=0
sqa=a*a
while(a):
    d=a%10
    s=s*10+d
    a//=10
sqs=s*s
revsqs=0
while(sqs):
    d=sqs%10
    revsqs=revsqs*10+d
    sqs//=10
if(sqa==revsqs):
    print(True)
else:
    print(False)