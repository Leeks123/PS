import sys
from collections import Counter

n = int(input())

books = []
for _ in range(n):
    books.append(sys.stdin.readline().rstrip())

counter = Counter(books)

arr = counter.most_common()
arr.sort(key=lambda x: (-x[1], x[0]))

print(arr[0][0])
