n = int(input())

peoples = []
for _ in range(n):
    name, day, month, year = input().split()
    peoples.append((name, int(day), int(month), int(year)))

peoples.sort(key=lambda x: (x[3], x[2], x[1]))

print(peoples[-1][0])
print(peoples[0][0])
