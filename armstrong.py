#m
x=int(input())
sum=0
temp=x
while(temp>0):
    c=temp%10
    sum=sum+c**3
    temp=temp//10
if(x==sum):
    print("yes")
else:
    print("no")
