
def prime(k):
    if k==1:
        return False
    for i in range(2,int(k**(1/2))+1):
        if k%i==0:
            return False
    return True
n=int(input())
l=[]
for i in range(1,n+1):
    if n%i==0:
        l.append(i)
cnt=0
for i in l:
    if not prime(i):
        cnt+=1
print(cnt) 
