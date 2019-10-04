# def solution(s):
#     answer = int(s)
    
#     return answer

# int()안쓰고 만들어보기
def solution(s):
    answer = 0

    for idx, num in enumerate(s[::-1]):
        if num == '-':
            answer *= -1
        else:
            answer += int(num) * (10 ** idx)

    return answer

if __name__ == '__main__':
    s = '-1234'
    print(solution(s))
    