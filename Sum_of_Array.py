
n=int(input())
l=list(map(int,input().split()))
a=[0]
for i in l:
    a.append(a[-1]+i)

print(a[-1]) 
