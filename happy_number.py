n=int(input())
while True:
    s=0
    while n>0:
        r=n%10
        n=n//10
        s+=r**2
    n=s
    if n<=9:
       break
if n==1 or n==7:
        print("True")
else:
        print("False")