
n=int(input())
sq=str(n**2)
sm=0
while n:
    rem=n%10
    sm=sm*10+rem
    n//=10

if str(sm**2)==sq[::-1]:
    print(True)
else:
    print(False)
    


