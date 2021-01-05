n, k  = map(int,input().split())

data = [x for x in range(2,n+1)]
cnt = 0
p = 2
i = 1
ret = 0

while True:
    while p*i<=n:
        if p*i in data:
            data.remove(p*i)
            cnt+=1
            # print(cnt,p*i)
            if cnt==k:
                ret=p*i
                break
        i+=1
    if len(data)==0:
        break
    p=data[0]
    i=1
    if ret!=0:
        break

print(ret)