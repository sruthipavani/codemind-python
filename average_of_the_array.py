n=int(input())
arr=list(map(int,input().split()))
avg=sum(arr)/n
k="{:.2f}".format(avg)
print(k)