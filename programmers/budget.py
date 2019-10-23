import heapq

def solution(d, budget):
    answer = 0
    
    heapq.heapify(d)
    element = heapq.heappop(d)
    while budget >= element :
        budget -= element
        answer += 1

        if not d :
            break
        element = heapq.heappop(d)
        
    return answer

if __name__ == '__main__':
    d = [1,3,2,5,4,2]
    budget = 9
    print(solution(d, budget))
    