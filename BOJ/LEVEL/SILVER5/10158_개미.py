w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())

x = t - (w-p)
y = t - (h-q)

if (x//w) % 2 == 0:
    x = w-(x % w)
else:
    x = x % w

if (y//h) % 2 == 0:
    y = h-(y % h)
else:
    y = y % h

print(x, y)

# 시간 초과
# dx = 1
# dy = 1
# move = 0

# while True:
#     if move == t:
#         break
#     # print(p, q, dx, dy)
#     if p+dx >= 0 and q+dy >= 0 and p+dx <= w and q+dy <= h:
#         # print('go')
#         p += dx
#         q += dy
#         move += 1
#     else:
#         # print('change direction')
#         if p+dx < 0 or p+dx > w:
#             dx *= -1
#         if q+dy < 0 or q+dy > h:
#             dy *= -1

# print(p, q)
