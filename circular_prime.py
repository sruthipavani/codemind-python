
def prime(p):
    if p==1:
        return False
    for i in range(2,int(p**(1/2))+1):
        if p%i==0:
            return False
    return True
def rev(p):
    s=0
    while p:
        r=p%10
        s=s*10+r
        p//=10
    return s 
n=int(input())
k=rev(n) 
if prime(n) and prime(k):
    print("circular prime")
elif not prime(n):
    print("not prime")
else:
    print("prime but not a circular prime")
