
def prime(k):
    if k==1:
        return False
    for i in range(2,int(k**(1/2))+1):
        if k%i==0:
            return False
    return True
n=int(input())
temp=n
f=0
while n:
    r=n%10
    if not prime(r):
        f=1
        break
    n//=10
if f==0 and prime(temp):
     print("Mega Prime")
else:
    print("Not Mega Prime") 
    
