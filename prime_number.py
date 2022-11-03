
def prime(k):
    if k==1:
        return False
    for i in range(2,int(k**(1/2))+1):
        if k%i==0:
            return False
    return True
n=int(input())
if prime(n):
    print("prime")
else:
    print("not a prime") 
