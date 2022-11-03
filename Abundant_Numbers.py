n=int(input())
sm=0
for i in range(1,n//2+1):
    if n%i==0:
        sm+=i
print(True) if sm>n else print(False)
