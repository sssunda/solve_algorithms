from itertools import combinations
import operator

def solution(relation):
    answer = []
    find_idx = []

    pivot_relation = [[]* n for n in range(len(relation[0]))]
    pivot_dic = {}

    # pivot_idexing
    for row_idx, row in enumerate(relation) :
        for idx in range(len(pivot_relation)):
            pivot_dic[(idx, row[idx])] = pivot_dic.get((idx, row[idx]), (row_idx+1)*(10**idx))
            pivot_relation[idx].append(pivot_dic[(idx, row[idx])])
    
    # make cases
    col = [n for n in range(len(pivot_relation))]
    col_combination = []
    for idx in range(len(relation[0])):
        col_combination += list(combinations(col, idx+1))
    
    # find index
    for col_ in col_combination:
        temp = [0 * n for n in range(len(pivot_relation))]
        for idx in col_:
            temp = list(map(operator.add, temp, pivot_relation[idx]))
        if unique(temp) :
            find_idx.append(col_)

    # deduplication
    for col in find_idx:
        if len(answer) == 0 :
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

    return answer


def unique(array):
    if len(set(array)) == len(array):
        return True
    return False


if __name__ == '__main__':
    relation = [["100","30","ryan","30","music","3"],
    ["200","40","apeach","40","music","3"],
    ["300","50","tube","30","computer","3"]]
    print(solution(relation))
    