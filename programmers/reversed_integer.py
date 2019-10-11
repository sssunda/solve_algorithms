def solution(n):
    n = list(str(n))
    n.sort(reverse=True)
    
    return int(''.join(n))

if __name__ == '__main__':
    n = 118372
    print(solution(n))

    