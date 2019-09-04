def solution(food_times, k):
    return eat(food_times, 0, 0, k, 1)


def eat(food_time, idx, cnt, k, direction):
    if idx > len(food_time) -1:
        idx = 0
    elif idx < 0:
        idx = len(food_time) + idx

    if cnt == k:
        return idx+1
    elif cnt != k and sum(food_time) == 0 :
        return -1

    food_time[idx] = food_time[idx]-1
    temp = idx + direction
    if temp > len(food_time) -1:
        temp = 0
    elif temp < 0:
        temp = len(food_time) - temp

    if food_time[temp] == 0:
        direction *= (-1)
                
    idx += direction
    return eat(food_time, idx, cnt+1, k, direction)


if __name__ == '__main__':
    food_times = [3,1,1,1,2,4,3]
    # food_times = [3,1,2]
    k =12
    print(solution(food_times, k))
