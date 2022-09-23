n=int(input())
c=0
c1=0
to=0
while n>0:
    r=n%10
    if r%2==0:
        c+=1
    else:
        c1+=1
    to+=1
    n=n//10
if c1==to:
    print("Odd")
elif c==to:
    print("Even")
else:
    print("Mixed")
    