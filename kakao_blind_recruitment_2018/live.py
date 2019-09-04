def solution(food_times, k):
    return eat(food_times, 0, 0, k)


def eat(food_time, idx, cnt, k):
    if idx > len(food_time) -1:
        idx = 0
        
    if cnt == k:
        if food_time[idx] == 0 :
            return eat(food_time, idx+1, cnt, k)
        return idx+1
    elif cnt != k and sum(food_time) == 0 :
        return -1
    
    if food_time[idx] == 0:
        return eat(food_time, idx+1, cnt, k)
                
    food_time[idx] = food_time[idx]-1
    return eat(food_time, idx+1, cnt+1, k)


if __name__ == '__main__':
    food_times = [3,1,1,1,2,4,3]
    # food_times = [3,1,2]
    k = 12
    print(solution(food_times, k))
