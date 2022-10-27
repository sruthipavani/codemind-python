N=int(input())
arr=list(map(int,input().split()))
s=sum(arr)
for i in range(N):
    if(s%N==0):
        print(N)
        break
    else:
        N=N-1