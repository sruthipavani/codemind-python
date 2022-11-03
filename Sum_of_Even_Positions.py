
n=int(input())
l=list(map(int,input().split()))
s=0
for ind,ele in enumerate(l):
    if ind%2==0:
        s+=ele

print(s)
