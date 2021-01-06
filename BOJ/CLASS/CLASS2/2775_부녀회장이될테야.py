t = int(input())

apartment = [[1]*14 for _ in range(15)]
apartment[0] = [x+1 for x in range(14)]

for floor in range(1, 15):
    for room in range(0, 14):
        apartment[floor][room] = sum(apartment[floor-1][0:room+1])

answers = []

for i in range(t):
    k = int(input())
    n = int(input())
    answers.append(apartment[k][n-1])

for answer in answers:
    print(answer)
