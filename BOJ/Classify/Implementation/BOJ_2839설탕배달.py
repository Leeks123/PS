n = int(input())

div5 = n//5
mod5 = n%5
ret = []

for i in range(div5+1):
    if (n-5*i)%3==0:
        ret.append(i+(n-5*i)//3) 

print(-1 if len(ret)==0 else min(ret))
