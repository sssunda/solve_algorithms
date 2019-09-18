def solution(s):
    pos = len(s) // 2
    # if it is even,
    if len(s) % 2 == 0:
        return s[pos-1:pos+1]
    
    return s[pos]
    # return s[(len(s)-1)//2 : len(s)//2 + 1]
if __name__ == '__main__':
    s = "abcde"
    print(solution(s))
    
