n = int(input())

company = set([])
for _ in range(n):
    name, action = input().split()
    if action == 'enter':
        company.add(name)
    else:
        company.remove(name)

company = list(company)
company.sort(reverse=True)
for i in company:
    print(i)
