t = int(input())


def calc():
    n = int(input())
    arr = []
    for _ in range(n):
        name, value = input().split()
        arr.append((name, int(value)))
    arr.sort(key=lambda x: x[1])
    return arr[-1][0]


for _ in range(t):
    print(calc())
