n=int(input())
arr=list(map(int,input().split()))
s_even,s_odd=0,0
for i in range(len(arr)):
    if i%2:
        s_odd+=arr[i]
    else:
        s_even+=arr[i]

print(abs(s_even-s_odd))
