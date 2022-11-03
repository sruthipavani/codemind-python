
def last_even(n,arr):
    for i in reversed(arr):
        if i%2==0:
            return i
            
            
n=int(input())
arr=list(map(int,input().split()))
res=last_even(n,arr)
print(res)

