t = int(input())

answers = []
for i in range(t):
    h,w,n = map(int,input().split())
    cnt = 0
    for x in range(1,w+1):
        for y in range(1,h+1):
            cnt+=1
            if cnt==n:
                answers.append(str(y)+(str(x) if len(str(x))==2 else "0"+str(x)))
                break

for answer in answers:
    print(answer)