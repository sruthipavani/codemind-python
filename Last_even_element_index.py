n=int(input())
arr=list(map(int,input().split()))
a=0
for i in range(n):
    if arr[i]%2==0:
        a=i
print(a)