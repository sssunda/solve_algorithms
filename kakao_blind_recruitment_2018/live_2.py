def solution(food_times, k):
    # sorted time
    sorted_times = sorted(food_times)
    
    last_time = 0
    len_foodtime = len(food_times)

    for time in sorted_times :
        spend_time = (time - last_time)*len_foodtime

        if spend_time <= k :
            k -= spend_time
            len_foodtime -= 1
            last_time = time
        else :
            k %= len_foodtime

            rest_time = []
            for idx in range(len(food_times)):
                if food_times[idx]>=time :
                    rest_time.append(idx)
            
            return rest_time[k] +1

    return -1


if __name__ == '__main__':
    # food_times = [3, 1, 1, 4, 3]
    # food_times = [3, 1, 2]
    food_times = [3,1,1,1,2,4,3]
    k = 12
    print("정답" , solution(food_times, k))
