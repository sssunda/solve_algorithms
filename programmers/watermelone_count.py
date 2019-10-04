def solution(n):
    pattern = '수박'
    answer = pattern*((n//2)+1)
    return answer[:n]

if __name__ == '__main__':
    n = 3
    print(solution(n))
    