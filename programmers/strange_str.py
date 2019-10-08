def solution(s):
    answer = []
    s = s.split(' ')

    for element in s :
        temp = ''
        for idx, e in enumerate(element):
            if idx % 2 == 0 :
                temp += e.upper()
            else :
                temp += e.lower()
        answer.append(temp)

    return ' '.join(answer)

if __name__ == '__main__':
    s = 'try hello world'
    print(solution(s))
    