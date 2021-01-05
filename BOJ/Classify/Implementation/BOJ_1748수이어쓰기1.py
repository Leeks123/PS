import math

n = int(input())
cnt = 0

d = len(str(n))

cnt+= (n - math.pow(10,d)+1)*d

for i in range(d):
    cnt+= 9*math.pow(10,i)*(i+1) 


print(int(cnt))
