from collections import Counter

n = int(input())

cards = []

for _ in range(n):
    cards.append(int(input()))

counter = Counter(cards)

arr = counter.most_common()
filtered = []
for i in range(len(arr)):
    if arr[i][1] == arr[0][1]:
        filtered.append(arr[i])

filtered.sort(key=lambda x: x[0])

print(filtered[0][0])
