
n=int(input())
a=[]
while (n>0):
    r=n%10
    a.append(r)
    n//=10
a.reverse()
for i in range(0,len(a)):
    if (a[i]==6):
        a[i]=9
        break
s=[str(i) for i in a]
b="".join(s)
print(b)

