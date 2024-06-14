x=tuple(map(int,input().split()))
count=len(x)-1
res=0
j=len(str(x[0]))
for i in x:
    res+=i*(10**(count*j))
    count-=1
print(res)