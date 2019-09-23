import re

def solution(s):
    pattern = re.compile('^[\d{4}|\d{6}]$')

    if pattern.match(s):
        return True
        
    return False


if __name__ == '__main__':
    s = '4232341'
    print(solution(s))

"""
def solution(s):
    return s.isdigit() and len(s) in (4, 6)
"""    