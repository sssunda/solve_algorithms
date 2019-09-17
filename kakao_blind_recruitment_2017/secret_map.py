def solution(n, arr1, arr2):
    answer = [''*m for m in range(n)] 
    
    for i in range(n):
        result_1 = str(bin(arr1[i]))[2:].rjust(n,'0')
        result_2 = str(bin(arr2[i]))[2:].rjust(n,'0')
        
        for j in range(n):
            if result_1[j] == '1' or result_2[j] == '1' :
                answer[i] += '#'
            else :
                answer[i] += ' '  

    return answer


if __name__ == '__main__':
    n = 5
    arr1 = [9, 20, 28, 18, 11]
    arr2 = [30, 1, 21, 17, 28]     
    print(solution(n, arr1, arr2))
    # divide(5, 9)

    