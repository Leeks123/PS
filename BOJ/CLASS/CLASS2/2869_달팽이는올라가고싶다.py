import math
up, down, top = map(int,input().split())

day = math.ceil( (top-down)/(up-down) )
print(day)