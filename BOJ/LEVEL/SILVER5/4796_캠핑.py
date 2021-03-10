i = 1
answers = []
while True:
    l, p, v = map(int, input().split())
    if l == 0 and p == 0 and v == 0:
        break

    answer = (v//p)*l + (v % p if v % p < l else l)
    answers.append((answer, i))
    i += 1

for a in answers:
    print('Case', str(a[1])+':', a[0])
