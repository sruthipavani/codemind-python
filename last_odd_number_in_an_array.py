n=int(input())
arr=list(map(int,input().split()))
x=0
for i in range(len(arr)):
    if arr[i]%2!=0:
        x=arr[i]
print(x)        