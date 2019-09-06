def solution(dartResult):
    bonus ={'S':1, 'D':2, 'T':3, '*': 2, '#':-1}
    dart = []
    result = [0]*3
    idx = 0

    temp = ""
    for element in dartResult :
        if element.isdigit():
            temp += element
            if len(dart) % 3 != 0 :
                dart.append(1)
        else :
            if len(temp) > 0 :
                dart.append(int(temp))
                temp = ""
            dart.append(bonus[element])

    if len(dart) != 9 :
        dart.append(1)

    # calculate
    idx = 0
    value = 1
    for dart_idx, element in enumerate(dart) :
        if dart_idx == 0 or dart_idx % 3 == 0 :
            value *= element
            continue
        elif dart_idx % 3 == 1 :
            value = value ** int(element)
            continue
        elif dart_idx % 3 == 2 :
            result[idx] = value
            value = 1
            
            result[idx] = result[idx] * element
            if element > 0 and idx != 0:
                result[idx-1] = result[idx-1] * element
            idx += 1                    

    return sum(result)

if __name__ == '__main__':
    dartResult = "1D2S#10S"
    print(solution(dartResult))
    