n=int(input())
mx=0
while n>0:
    r=n%10
    if r>mx:
        mx=r
    n=n//10
print(mx)    