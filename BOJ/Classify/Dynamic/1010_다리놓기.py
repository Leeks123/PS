# ===== 메모리 초과 ========
# from itertools import combinations
# t = int(input())

# answer = []
# for _ in range(t):
#     n, m = map(int, input().split())
#     data = [x for x in range(m)]
#     result = list(combinations(data, n))
#     answer.append(len(result))

# for a in answer:
#     print(a)

# python 3.8
import math

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    print(math.comb(m, n))
