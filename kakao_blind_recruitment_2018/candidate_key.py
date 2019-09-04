from itertools import combinations

def solution(relation):
    answer = []
    len_col = [x for x in range(len(relation[0]))]
    col = []
    for idx in range(len(len_col)):
        col+=list(combinations(len_col, idx+1))
    copy_col = col[:]

    for idx in col :
        temp = []
        for element in relation :
            temp_col = []
            for i in idx :
                temp_col.append(element[i])
            temp.append(tuple(temp_col))
        if len(set(temp)) != len(relation):
            copy_col.remove(idx)
    
    for col in copy_col :
        if len(answer) == 0:
            answer.append(col)
        else :
            flag = False
            for a in answer :
                temp = set(col)-set(a)
                if len(temp) == len(col)-len(a):
                    flag = False
                    break
                else :
                    flag = True
                    continue
            if flag :
                answer.append(col)

    return len(answer)


if __name__ == '__main__':
    relation = [["100","30","ryan","30","music","3"],
    ["200","40","apeach","40","music","3"],
    ["300","50","tube","50","computer","3"],
    ["400","60","con","60","computer","4"],
    ["500","70","muzi","70","music","3"],
    ["600","80","apeach","80","music","2"]]

    # relation = [["a","b","c"], ["1","b","c"], ["a","b","4"], ["a","5","c"]]
    # relation = [["a","1","4"], ["2","1","5"], ["a","2","4"]]
    print(solution(relation))
    