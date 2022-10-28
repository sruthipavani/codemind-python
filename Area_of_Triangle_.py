A,B,C=map(float,input().split())
s=(A+B+C)/2
area=(s*(s-A)*(s-B)*(s-C))**0.5
print("{:.2f}".format(area))