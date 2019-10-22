def solution(num):
    cnt = 0
    
    while num != 1 :
        if cnt > 500 :
            cnt = -1
            break

        # 짝수일 경우,
        if num % 2 == 0 :
            num = num // 2
        # 홀수일 경우,
        else :
            num = (num * 3) + 1
        cnt += 1

    return cnt

if __name__ == '__main__':
    num = 16
    solution(num)
    
