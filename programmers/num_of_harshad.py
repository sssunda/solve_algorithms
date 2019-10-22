def solution(x):
    num = 0

    for element in str(x) :
        num += int(element)
    
    if x % num == 0 :
        return True

    return False

if __name__ == '__main__':
    x = 13
    print(solution(x))
    