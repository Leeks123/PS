n = list(input())

if '0' in n:
    n = list(map(int, n))
    if sum(n) % 3 == 0:
        n.sort(reverse=True)
        print(''.join(list(map(str, n))))
    else:
        print(-1)
else:
    print(-1)
