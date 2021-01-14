n, m = map(int, input().split())
trees = list(map(int, input().split()))

start = 0
end = max(trees)
answer = 0


def cutTree(trees, height):
    result = 0
    for tree in trees:
        if tree > height:
            result += tree-height
    return result


while start <= end:
    mid = (start+end)//2
    result = cutTree(trees, mid)
    print(start, mid, end, result)
    if result >= m:
        start = mid+1
        answer = mid
    else:
        end = mid-1

print(answer)
