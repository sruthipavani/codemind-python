
n=int(input())
a=[]
while(n>0):
    r=n%10
    a.append(r)
    n=n//10

if( len(a)==len(set(a))):
    print("Unique Number")
else:
    print("Not Unique Number")
    

