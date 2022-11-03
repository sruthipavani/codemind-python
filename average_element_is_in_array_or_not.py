n=int(input())
l=list(map(int,input().split()))
a=int(sum(l)/len(l))
f=0
for i in range(len(l)):
    if l[i]==a:
        f=1
if f==1:
    print("True")
else:
    print("False")