def solution(s, n):
    answer = ''

    for element in s :
        if ord(element) == 32 :
            answer += ' '
            continue
        # 대문자인 경우,
        if element.isupper() :
            answer += chr((ord(element)-ord('A')+ n)%26+ord('A'))
        # 소문자인 경우,            
        else :
            answer += chr((ord(element)-ord('a')+ n)%26+ord('a'))

    return answer

if __name__ == '__main__':
    s = 'z'
    n = 25
    print(solution(s, n))
    