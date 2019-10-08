def solution(n):
    answer = 0
    n_ = int(n ** 0.5) 
    for i in range (1, n_ + 1):
        if n % i == 0 :
            answer += i
            answer += n // i
    if n_ ** 2 == n :
        answer -= n_

    return answer

if __name__ == '__main__':
    n = 12
    print(solution(n))

    