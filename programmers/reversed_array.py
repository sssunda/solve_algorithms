def solution(n):
    n = str(n)[::-1]
    n = list(map(int, n))

    return n

if __name__ == '__main__':
    n = 1250
    print(solution(n))
    