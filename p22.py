#o
m,q=map(int,input().split())
y=min(m,q)
x=[]
for i in range(1,y+1):
    if((m%i==0) and (q%i==0)):
        x.append(i)
print(max(x))
