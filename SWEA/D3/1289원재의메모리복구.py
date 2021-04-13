t = int(input())


def solve(n):
    flag = 0
    count = 0
    for i in range(len(n)):
        if int(n[i]) != flag:
            flag = int(n[i])
            count += 1
    return count


for i in range(1, t+1):
    n = input()
    answer = solve(n)
    print('#'+str(i), answer)
