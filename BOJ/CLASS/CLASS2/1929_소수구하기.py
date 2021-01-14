n, m = map(int, input().split())


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


answer = [0]*(m+1)

for i in range(2, m+1):
    if answer[i] == -1:
        continue
    if isPrime(i):
        answer[i] = 1
        cnt = 2
        while True:
            if i*cnt > m:
                break
            answer[i*cnt] = -1
            cnt += 1

for i in range(n, m+1):
    if answer[i] == 1:
        print(i)
