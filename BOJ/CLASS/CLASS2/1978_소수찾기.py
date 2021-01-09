# 1978

n = int(input())

li = input().split(' ')


def isPrime(n):
    i = 2
    while i <= n:
        if n % i == 0:
            if n == i:
                return True
            else:
                return False
        else:
            i += 1
            continue


cnt = 0
for i in range(n):
    if isPrime(int(li[i])):
        cnt += 1

print(cnt)
