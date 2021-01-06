
answer = []
while True:
    tri = list(map(int,input().split()))
    if tri[0]==0 and tri[1]==0 and tri[2]==0:
        break
    tri.sort()
    a,b,c = tri
    if a**2+b**2 == c**2:
        answer.append("right")
    else:
        answer.append("wrong")

for s in answer:
    print(s)