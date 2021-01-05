from collections import deque

def qIng(n,m,documents):
    q = deque(documents)
    cnt = 0
    targetPos = m
    while len(q)!=0:
        cur = q.popleft()
        if len(q)==0:
            cnt+=1
            break
        if cur>=max(q):
            cnt+=1
            if targetPos==0:
                break
        else:
            q.append(cur)
        targetPos = (targetPos+len(q)-1)%len(q)
    return cnt

t = int(input())

answer = []
for i in range(t):
    n, m = map(int,input().split())
    documents = list(map(int,input().split()))
    answer.append(qIng(n,m,documents))

for i in answer:
    print(i)