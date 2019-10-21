def solution(arr):
    min_num = min(arr)
    arr.remove(min_num)
    
    if arr :
        return arr
    return [-1]

if __name__ == '__main__':
    arr = [1]
    print(solution(arr))
    