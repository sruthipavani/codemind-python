
import math
n=int(input())
total=n*n
k=int(math.log10(total)+1)
if k%2:
    k=k//2+1
else:
    k=k//2
res=""
while k: 
    r=total%10
    res+=str(r)
    total//=10
    k-=1
res=res[::-1]
#print(res) 
if int(res)==n:
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")
