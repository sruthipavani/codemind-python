
import math as M
n=int(input())
digit=int(M.log10(n)+1)
sm=0
temp=n
while n:
    rem=n%10
    sm+=rem**digit
    digit-=1
    n//=10
if sm==temp:
    print(True)
else:
    print(False)
    

