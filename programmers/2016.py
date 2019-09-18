def solution(a, b):
    WEEK = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    DAY = {1:31, 2:29, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}

    t_day = b
    for i in range(1,a):
        t_day += DAY[i]
    t_day %= 7

    return WEEK[t_day-1]

if __name__ == '__main__':
    a = 5
    b = 24
    print(solution(a, b))
    