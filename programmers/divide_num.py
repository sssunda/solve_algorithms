def solution(arr, divisor):
    arr.sort()
    answer = list(filter(lambda x : x % divisor == 0, arr))
    
    if answer :
        return answer

    return [-1]

if __name__ == '__main__':
    arr = [2, 36, 1, 3]
    divisor = 1
    solution(arr, divisor)
    