a,b=map(int,input().split())
def lcm(a,b):
    if b>a:
        g=b
    else:
        g=0
    while True:
            if g%a==0 and g%b==0:
                lcm=g
                break
            else:
                g+=1
    return lcm
y=(a*b)//lcm(a,b)
print(y)