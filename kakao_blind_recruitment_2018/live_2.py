def solution(food_times, k):
    times = {}
    times_copy = {}
    for idx, time in enumerate(food_times):
        times[time] = times.get(time, [])+[idx]
        times_copy[time] = times_copy.get(time, [])+[idx]

    last_time = 0
    len_foodtime = len(food_times)

    for time in sorted(times):
        spend_time = (time - last_time) * len_foodtime
        if spend_time <= k :
            k -= spend_time
            len_foodtime -= len(times[time])
            last_time = time
            del times_copy[time]

        else :
            k %= len_foodtime
            rest_time = []    
            for element in times_copy.values() :
                rest_time += element
            return sorted(rest_time)[k]+1

    return -1



if __name__ == '__main__':
    food_times = [3, 1, 1, 4, 3]
    # food_times = [3, 1, 2]
    k = 3
    print(solution(food_times, k))

