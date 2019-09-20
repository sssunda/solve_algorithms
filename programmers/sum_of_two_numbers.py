def solution(a, b):
    if a > b:
        a, b = b, a
    answer = sum([x for x in range(a, b+1)])
    return answer

if __name__ == '__main__':
    a = 3
    b = 3
    print(solution(a,b))
    