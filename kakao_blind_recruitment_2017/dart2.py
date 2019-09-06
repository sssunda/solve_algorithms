import re
def solution(dartResult):
    digit_pattern = '[SDT]{1}[*#]?'
    bonus = {'S':1, 'D':2, 'T':3}
    options = {'*': 2 , '#':-1}

    digit = re.split(digit_pattern, dartResult)
    digit = list(map(lambda  x: int(x), filter(lambda x: len(x)>0 ,digit)))
    idx = 0
    for element in dartResult :
        if not element.isdigit():
            if element in bonus.keys():
                digit[idx] = digit[idx] ** bonus[element]
                idx += 1
                continue
            else :
                digit[idx-1] = digit[idx-1] * options[element]
                if idx != 1 and options[element]>0 :
                    digit[idx-2] = digit[idx-2] * options[element]
            
    return sum(digit)

if __name__ == '__main__':
    dartResult = "1D2S#10S"
    
    print(solution(dartResult))
    