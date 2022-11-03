
def isprime(k):
    if k==1:
        return False
    else:
        for i in range(2,int(k**(1/2))+1):
            if k%i==0:
                return False
    return True
cnt=0
l=int(input())
r=int(input())
for i in range(l,r+1):
    if isprime(i):
        cnt+=1
print(cnt) 
