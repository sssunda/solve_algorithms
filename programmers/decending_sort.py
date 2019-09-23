def solution(s):
    upper = []
    lower = []

    for element in s :
        # upper case
        if ord(element) <= 90 :
            upper.append(element)
        # lower case
        else :
            lower.append(element)
    
    upper.sort(reverse = True)
    lower.sort(reverse = True)
    
    return ''.join(lower) + ''.join(upper)

if __name__ == '__main__':
    s = 'aAZbcdefg'
    print(solution(s))
"""
def solution(s):
    return ''.join(sorted(s, reverse=True))
"""    