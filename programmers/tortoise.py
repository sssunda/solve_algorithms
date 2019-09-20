def solution(m, n, puddles):
    # create map 
    directions = [[1]*(m+2)]
    for i in range(n):
        directions.append([1])
        directions[i+1] += [0] * m
        directions[i+1] += [1]
    directions.append([1]*(m+2))

    for puddle in puddles :
        directions[puddle[1]][puddle[0]] = 1

    # definition
    END = (n, m)
    result = {}

    get_route(1, 1, directions, END, -1, result)
    
    if result :
        key = sorted(result.keys())[0]
        return result[key] % 1000000007
    return 0

def get_route(x, y, directions, END, cnt, result):
    if (x, y) == END :
        result[cnt] = result.get(cnt, 0) + 1
        return True

    pos_x = (0, 1)
    pos_y = (1, 0)
    for i in range(2):
        dx = x + pos_x[i]
        dy = y + pos_y[i]
        if dx > END[0] or dy > END[1] or directions[dx][dy] == 1:
            continue
        get_route(dx, dy, directions, END, cnt+1, result)
        
    
if __name__ == '__main__':
    m = 4
    n = 3
    puddles = [[2,2]]
    print(solution(m, n, puddles))