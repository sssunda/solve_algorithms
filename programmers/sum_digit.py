def solution(n):
    n = sum(map(lambda x: int(x), str(n)))

    return n


if __name__ == '__main__':
    n = 987
    print(solution(n))