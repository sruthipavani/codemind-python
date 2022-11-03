
def selfDividingNumbers(left,right):
        def self_divide(n):
            temp=n
            while n:
                rem=n%10
                if rem==0 or temp%rem!=0:
                    return 0
                else:
                   n//=10
            return 1
        
        lst=[]
        for i in range(left,right+1):
            if self_divide(i):
                lst.append(i)
        return lst
left=int(input())
right=int(input())
res=selfDividingNumbers(left,right)
for i in res:
    print(i,end=" ") 

