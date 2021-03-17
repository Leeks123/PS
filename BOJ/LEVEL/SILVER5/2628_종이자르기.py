w, h = map(int, input().split())

cut = int(input())

cutWidthPos = []
cutHeightPos = []

for _ in range(cut):
    cat, value = map(int, input().split())
    if cat == 1:
        cutWidthPos.append(value)
    else:
        cutHeightPos.append(value)

cutWidthPos.sort()
cutHeightPos.sort()

cuttedWidth = [cutWidthPos[0], ] if len(cutWidthPos) != 0 else []
cuttedHeight = [cutHeightPos[0], ] if len(cutHeightPos) != 0 else []

for i in range(1, len(cutWidthPos)):
    cuttedWidth.append(cutWidthPos[i]-cutWidthPos[i-1])
    if i == len(cutWidthPos)-1:
        cuttedWidth.append(w-cutWidthPos[i])
if len(cutWidthPos) == 1:
    cuttedWidth.append(w-cuttedWidth[0])

for i in range(1, len(cutHeightPos)):
    cuttedHeight.append(cutHeightPos[i]-cutHeightPos[i-1])
    if i == len(cutHeightPos)-1:
        cuttedHeight.append(h-cutHeightPos[i])
if len(cutHeightPos) == 1:
    cuttedHeight.append(w-cuttedHeight[0])

# print(cuttedHeight, cuttedWidth)
print(max(cuttedHeight if len(cuttedHeight) != 0 else [h])
      * max(cuttedWidth if len(cuttedWidth) != 0 else [w]))
