def solution(n, m):
    max_num = max([n, m])
    unit = []
    
    for i in range(1, max_num + 1):
        if n % i == 0 and m % i == 0 :
            unit.append(i)
    
    gcd = max(unit)
    lcm = n * m // gcd
    
    return [gcd, lcm]

if __name__ == '__main__':
    n = 6
    m = 12
    print(solution(n, m))
    