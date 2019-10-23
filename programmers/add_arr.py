import operator
def solution(arr1, arr2):
    answer = []
    for idx in range(len(arr1)):
        answer.append(list(map(operator.add, arr1[idx], arr2[idx])))

    return answer

if __name__ == '__main__':
    arr1 = [[1,2],[2,3]]
    arr2 = [[1,2],[2,3]]
    print(solution(arr1, arr2))
    