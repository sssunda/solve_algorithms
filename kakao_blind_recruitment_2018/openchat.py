def solution(record):
    answer = []
    stack = []
    user = {}
    state = {'Enter' : '님이 들어왔습니다.', 'Leave': '님이 나갔습니다.'}

    for element in record :
        element = element.split(" ")
        if element[0] == "Enter" or element[0] == "Change" :
            user[element[1]] = element[2]
        
        stack.append((element[0],element[1]))
    
    for element in stack :
        if element[0] != "Change":
            answer.append(user[element[1]]+state[element[0]])

    return answer

if __name__ == '__main__':
    record = ["Enter uid1234 Muzi", 
    "Enter uid4567 Prodo",
    "Leave uid1234",
    "Enter uid1234 Prodo",
    "Change uid4567 Ryan"]

    print(solution(record))
