n, m = map(int, input().split())

dic = {}
for _ in range(n):
    s = input().split()
    dic[s[0]] = s[1]

answer = []
for _ in range(m):
    answer.append(dic[input()])

for i in range(m):
    print(answer[i])
