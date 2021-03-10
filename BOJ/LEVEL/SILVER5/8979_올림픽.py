countries, wantToKnow = map(int, input().split())

data = []

for _ in range(countries):
    countryNum, gold, silver, bronze = map(int, input().split())
    data.append([countryNum, gold, silver, bronze])

data.sort(key=lambda x: x[3], reverse=True)
data.sort(key=lambda x: x[2], reverse=True)
data.sort(key=lambda x: x[1], reverse=True)

prevCountry = [data[0][1:], 1]
grade = 1
for i in range(0, len(data)):
    if prevCountry[0] != data[i][1:]:
        grade = i+1
        prevCountry = [data[i][1:], grade]
    if data[i][0] == wantToKnow:
        break

# print(data)
print(grade)
