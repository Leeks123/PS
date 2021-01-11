
k = int(input())

data = []
for i in range(k):
    n = int(input())
    if n == 0:
        if not len(data) == 0:
            data.pop(len(data)-1)
    else:
        data.append(n)

print(0 if len(data) == 0 else sum(data))
