import itertools

n, m = map(int,input().split())
cards = list(map(int,input().split()))

answer = 0
for x in itertools.combinations(cards,3):
    if m<sum(list(x)): continue
    if m-sum(list(x)) < m-answer:
        answer = sum(list(x))

print(answer)