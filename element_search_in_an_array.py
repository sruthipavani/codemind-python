n=int(input())
arr=list(map(int,input().split()))
k=int(input())
s=0
for i in arr:
    if i==k:
        print(True)
        s=1
        break
if(s==0):
    print(False)