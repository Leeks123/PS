n, m = map(int, input().split())

candidates = []
for _ in range(n):
    arr = list(map(int, input().split()))
    candidates.append(min(arr))

print(max(candidates))
