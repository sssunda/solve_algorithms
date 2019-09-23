def solution(s):
    word_dict = {}
    
    for element in s.lower():
        word_dict[element] = word_dict.get(element, 0) + 1
    
    if word_dict.get('p', 0) == word_dict.get('y', 0):
        return True  
    
    return False


if __name__ == '__main__':
    s = 'pPoooyY'
    print(solution(s))
"""
def solution(s):
    return s.lower().count('p') == s.lower().count('y')
"""