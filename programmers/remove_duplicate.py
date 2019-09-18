def solution(arr):
    answer = []
    stack = [arr[0]]

    for element in arr[1:] :
        if element != stack[-1] :
            answer.append(stack[-1])
            stack = [element]
            
    if stack :
        answer.append(stack[-1])

    return answer

if __name__ == '__main__':
    arr = [4,4,4,3,3]
    print(solution(arr))
    