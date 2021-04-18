# 효율성 테스트 실패
def solution(food_times, k):
    ptr = 0
    if sum(food_times) <= k:
        return -1
    for i in range(1, k+1):
        while food_times[ptr] == 0:
            ptr = (ptr+1) % len(food_times)
        food_times[ptr] -= 1
        ptr = (ptr+1) % len(food_times)

    if food_times[ptr] == 0:
        while food_times[ptr] == 0:
            ptr = (ptr+1) % len(food_times)
        return ptr + 1
    return ptr + 1
