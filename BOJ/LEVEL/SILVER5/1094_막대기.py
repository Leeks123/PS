n = int(input())

bars = [64, ]

if sum(bars) > n:
    while sum(bars) != n:

        smallestBar = bars.pop()
        if sum(bars)+smallestBar//2 >= n:
            bars.append(smallestBar//2)
        else:
            bars.append(smallestBar // 2)
            bars.append(smallestBar // 2)


print(len(bars))
