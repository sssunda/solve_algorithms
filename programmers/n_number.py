def solution(x, n):
    answer = [i * x + x for i in range(n)]
    
    return answer

if __name__ == '__main__':    
    x = -4
    n = 2
    print(solution(x,n))