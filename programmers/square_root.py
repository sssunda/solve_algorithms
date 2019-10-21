def solution(n):
    root_num = int(n ** (0.5))
    if root_num ** 2 == n :
        return (root_num + 1) ** 2
    return -1

if __name__ == '__main__':
    n = 121
    print(solution(n))